import os
import re
from yt_dlp import YoutubeDL
import json
import tempfile
from PIL import Image
import io
import base64

from src.models.media_model import MediaModel


class ProgressHook:
    def __init__(self, progress_frame=None, app=None):
        self.progress_frame = progress_frame
        self.app = app
        self.downloaded_bytes = 0
        self.total_bytes = 0
        self.speed = 0
        self.eta = 0
        self.status = "Waiting"
        self.filename = ""
        self.percent = 0

    def __call__(self, d):
        if d["status"] == "downloading":
            self.status = "Downloading..."
            self.downloaded_bytes = d.get("downloaded_bytes", 0)
            self.total_bytes = d.get("total_bytes") or d.get("total_bytes_estimate", 0)
            self.speed = d.get("speed", 0)
            self.eta = d.get("eta", 0)
            self.filename = d.get("filename", "")

            if self.total_bytes > 0:
                self.percent = (self.downloaded_bytes / self.total_bytes) * 100
            else:
                self.percent = 0

            # Direct UI update
            if self.progress_frame and self.app:
                self._update_ui_directly()

        elif d["status"] == "finished":
            self.status = "Finished downloading, now post-processing..."
            self.percent = 100

            if self.progress_frame and self.app:
                self._update_ui_directly()

        elif d["status"] == "error":
            self.status = f"Error: {d.get('error', 'Unknown error')}"
            self.percent = 0

            if self.progress_frame and self.app:
                self._update_ui_directly()

    def _update_ui_directly(self):
        """Update UI directly from the progress hook"""
        if not self.progress_frame or not hasattr(self.progress_frame, "progress_bar"):
            return

        try:
            # Format display text
            bytes_text = ""
            if self.total_bytes > 0:
                downloaded_mb = self.downloaded_bytes / (1024 * 1024)
                total_mb = self.total_bytes / (1024 * 1024)
                bytes_text = f" {downloaded_mb:.1f}/{total_mb:.1f} MB"

            speed_text = f"{self._format_speed(self.speed)}" if self.speed else ""
            eta_text = f", {self.eta}s remaining" if self.eta else ""
            status_text = f"{self.status}{bytes_text} {speed_text}{eta_text}"

            # Update UI elements
            def update():
                if hasattr(self.progress_frame, "progress_bar"):
                    self.progress_frame.progress_bar.set(
                        max(0, min(100, self.percent)) / 100
                    )
                if hasattr(self.progress_frame, "status_label"):
                    self.progress_frame.status_label.configure(text=status_text)

            # Schedule UI update on main thread
            self.app.after(0, update)

        except Exception:
            pass

    def _format_speed(self, bytes_per_second):
        """Format download speed for display"""
        if bytes_per_second < 1024:
            return f"{bytes_per_second:.0f} B/s"
        elif bytes_per_second < 1024**2:
            return f"{bytes_per_second/1024:.1f} KB/s"
        else:
            return f"{bytes_per_second/(1024**2):.1f} MB/s"


class Downloader:
    def __init__(self):
        self.progress_hooks = []
        self.last_progress = None

    def parse_youtube_link(self, url):
        """
        Extract metadata from YouTube URL without downloading
        Returns a dictionary with thumbnail URL, title, etc.
        """
        try:
            with YoutubeDL({"quiet": True, "no_warnings": True}) as ydl:
                info = ydl.extract_info(url, download=False)

                media = {
                    "title": info.get("title", "Unknown Title"),
                    "uploader": info.get("uploader", "Unknown Uploader"),
                    "duration": info.get("duration", 0),
                    "thumbnail": info.get("thumbnail", ""),
                    "formats": [],
                    "url": url,
                    "id": info.get("id", ""),
                    "description": info.get("description", ""),
                    "view_count": info.get("view_count", 0),
                    "like_count": info.get("like_count", 0),
                    "upload_date": info.get("upload_date", ""),
                }

                # Extract available formats with readable names
                for fmt in info.get("formats", []):
                    if fmt.get("resolution") and fmt.get("format_note") != "storyboard":
                        format_id = fmt.get("format_id", "")
                        res = fmt.get("resolution", "")
                        ext = fmt.get("ext", "")
                        vcodec = fmt.get("vcodec", "")
                        filesize = fmt.get("filesize", 0)

                        # Skip formats without actual video (audio only)
                        if vcodec != "none" and res:
                            media["formats"].append(
                                {
                                    "format_id": format_id,
                                    "resolution": res,
                                    "ext": ext,
                                    "filesize": (
                                        self._format_bytes(filesize)
                                        if filesize
                                        else "Unknown"
                                    ),
                                    "format_note": fmt.get("format_note", ""),
                                }
                            )

                # Also add audio-only formats
                for fmt in info.get("formats", []):
                    if fmt.get("vcodec") == "none" and fmt.get("acodec") != "none":
                        format_id = fmt.get("format_id", "")
                        acodec = fmt.get("acodec", "")
                        ext = fmt.get("ext", "")
                        filesize = fmt.get("filesize", 0)

                        media["formats"].append(
                            {
                                "format_id": format_id,
                                "resolution": "Audio only",
                                "ext": ext,
                                "filesize": (
                                    self._format_bytes(filesize)
                                    if filesize
                                    else "Unknown"
                                ),
                                "format_note": f"Audio ({acodec})",
                            }
                        )

                return media
        except Exception as e:
            return {"error": str(e)}

    def _format_bytes(self, bytes):
        """Convert bytes to human-readable form"""
        if bytes < 1024:
            return f"{bytes} B"
        elif bytes < 1024**2:
            return f"{bytes/1024:.1f} KB"
        elif bytes < 1024**3:
            return f"{bytes/(1024**2):.1f} MB"
        else:
            return f"{bytes/(1024**3):.1f} GB"

    def _get_format_string(self, quality):
        """Convert user-friendly quality options to yt-dlp format strings"""
        quality_map = {
            "Best": "bestvideo+bestaudio/best",
            "2160p (4K)": "bestvideo[height<=2160]+bestaudio/best[height<=2160]",
            "1440p (2K)": "bestvideo[height<=1440]+bestaudio/best[height<=1440]",
            "1080p (FHD)": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
            "720p (HD)": "bestvideo[height<=720]+bestaudio/best[height<=720]",
            "480p": "bestvideo[height<=480]+bestaudio/best[height<=480]",
            "360p": "bestvideo[height<=360]+bestaudio/best[height<=360]",
            "Audio Only": "bestaudio",
            "Best Audio": "bestaudio",
            "320k": "bestaudio[abr<=320]",
            "256k": "bestaudio[abr<=256]",
            "192k": "bestaudio[abr<=192]",
            "128k": "bestaudio[abr<=128]",
            "opus": "bestaudio[ext=opus]",
            "aac": "bestaudio[ext=aac]",
            "vorbis": "bestaudio[ext=vorbis]",
            "mp3": "bestaudio[ext=mp3]/bestaudio",
            "m4a": "bestaudio[ext=m4a]/bestaudio",
        }

        return quality_map.get(quality, "best")

    def _prepare_options(
        self,
        quality,
        destination,
        cookies=None,
        custom_args=None,
        progress_frame=None,
        app=None,
    ):
        """Prepare yt-dlp options with common settings"""
        # Create a new progress hook for this download with direct UI access
        progress_hook = ProgressHook(progress_frame, app)

        # Clear old hooks and add the new one
        self.progress_hooks.clear()
        self.progress_hooks.append(progress_hook)

        # Base options
        opts = {
            "format": self._get_format_string(quality),
            "outtmpl": os.path.join(destination, "%(title)s.%(ext)s"),
            "writethumbnail": True,
            "noplaylist": True,
            "progress_hooks": [progress_hook],
            "noprogress": False,
            "quiet": True,
            "no_warnings": True,
            "postprocessors": [
                {"key": "EmbedThumbnail", "already_have_thumbnail": False},
                {"key": "FFmpegMetadata"},
            ],
        }

        # Add audio conversion for audio-only downloads
        if quality in [
            "Audio Only",
            "Best Audio",
            "320k",
            "256k",
            "192k",
            "128k",
            "opus",
            "aac",
            "vorbis",
            "mp3",
            "m4a",
        ]:
            audio_format = "mp3"
            if quality in ["opus", "aac", "vorbis", "m4a"]:
                audio_format = quality

            opts["postprocessors"].append(
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": audio_format,
                    "preferredquality": (
                        "192"
                        if quality == "Best Audio"
                        else (
                            quality.replace("k", "")
                            if quality in ["320k", "256k", "192k", "128k"]
                            else "192"
                        )
                    ),
                }
            )

        # Add cookies if provided
        if cookies and os.path.exists(cookies):
            opts["cookiefile"] = cookies
        elif cookies:
            pass  # Cookies file not found, continue without it

        # Parse and add any custom arguments
        if custom_args:
            try:
                custom_args_dict = {}
                for arg in custom_args.split("--"):
                    if not arg.strip():
                        continue
                    parts = arg.strip().split(" ", 1)
                    if len(parts) == 1:
                        custom_args_dict[parts[0]] = True
                    else:
                        key, value = parts
                        custom_args_dict[key] = value

                # Merge custom args with default opts
                opts.update(custom_args_dict)
            except Exception as e:
                pass  # Continue without custom args if parsing fails

        return opts

    def download_video(
        self,
        url,
        quality,
        destination,
        cookies=None,
        custom_args=None,
        progress_frame=None,
        app=None,
    ):
        """Download a single video with the specified quality"""
        opts = self._prepare_options(
            quality, destination, cookies, custom_args, progress_frame, app
        )

        try:
            with YoutubeDL(opts) as ydl:
                ydl.download([url])
            return True, "Download completed successfully"
        except Exception as e:
            return False, str(e)

    def download_audio(
        self,
        url,
        quality,
        destination,
        cookies=None,
        custom_args=None,
        progress_frame=None,
        app=None,
    ):
        """Download audio with the specified quality"""
        # For audio downloads, ensure we have the audio extraction post-processor
        opts = self._prepare_options(
            quality, destination, cookies, custom_args, progress_frame, app
        )

        try:
            with YoutubeDL(opts) as ydl:
                ydl.download([url])
            return True, "Audio download completed successfully"
        except Exception as e:
            return False, str(e)

    def download_clip(
        self,
        url,
        start_time,
        end_time,
        quality,
        destination,
        cookies=None,
        custom_args=None,
        progress_frame=None,
        app=None,
    ):
        """Download a clip from a video with specified start and end times"""
        # Convert HH:MM:SS format to seconds
        start_seconds = self._time_to_seconds(start_time)
        end_seconds = self._time_to_seconds(end_time)

        if start_seconds < 0 or (end_seconds <= start_seconds and end_seconds > 0):
            return False, "Invalid time format or end time is before start time"

        opts = self._prepare_options(
            quality, destination, cookies, custom_args, progress_frame, app
        )

        # Add download range to options
        if end_seconds > 0:
            opts["download_ranges"] = lambda _, __: [(start_seconds, end_seconds)]
            # Format to include time range in filename
            opts["outtmpl"] = os.path.join(
                destination, f"%(title)s [{start_time}-{end_time}].%(ext)s"
            )
        else:
            # Only start time specified
            opts["download_ranges"] = lambda _, __: [(start_seconds, None)]
            opts["outtmpl"] = os.path.join(
                destination, f"%(title)s [from {start_time}].%(ext)s"
            )

        try:
            with YoutubeDL(opts) as ydl:
                ydl.download([url])
            return True, "Clip download completed successfully"
        except Exception as e:
            return False, str(e)

    def _time_to_seconds(self, time_str):
        """Convert HH:MM:SS or MM:SS format to seconds"""
        if not time_str or time_str.strip() == "":
            return -1

        try:
            # Handle different time formats
            time_parts = time_str.strip().split(":")
            if len(time_parts) == 3:  # HH:MM:SS
                h, m, s = time_parts
                return int(h) * 3600 + int(m) * 60 + int(s)
            elif len(time_parts) == 2:  # MM:SS
                m, s = time_parts
                return int(m) * 60 + int(s)
            else:  # SS only
                return int(time_str)
        except Exception:
            return -1

    def get_thumbnail(self, url):
        """Get thumbnail image for a video"""
        try:
            with YoutubeDL({"quiet": True, "no_warnings": True}) as ydl:
                info = ydl.extract_info(url, download=False)
                return info.get("thumbnail", "")
        except Exception as e:
            print(f"Error fetching thumbnail: {e}")
            return None

    def get_progress(self):
        """Get the latest progress information"""
        if not self.progress_hooks:
            return None

        return self.progress_hooks[-1]
