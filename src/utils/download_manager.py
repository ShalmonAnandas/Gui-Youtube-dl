from threading import Thread, Lock
from queue import Queue, Empty
import time
import os
import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
import requests
import io

from src.models.download_task import DownloadTask
from src.utils.download_manager_core import DownloadManagerCore
from src.utils.download_manager_ui import DownloadManagerUI
from src.utils.download_manager_multi import DownloadManagerMulti
from src.utils.downloader import Downloader


class DownloadManager:
    def __init__(self, app):
        self.app = app
        self.downloader = Downloader()
        self.ui = DownloadManagerUI(app)
        self.core = DownloadManagerCore(self.downloader, self._update_progress)
        self.multi = DownloadManagerMulti(self.downloader, self._update_progress)
        self.lock = Lock()  # Initialize a threading lock
        self.is_downloading = False  # Initialize the is_downloading flag
        self.queue = Queue()  # Initialize a queue for thread communication
        self.current_task = None  # Initialize the current_task attribute
        self.progress_callback = (
            self._update_progress
        )  # Set progress_callback to the _update_progress method
        self.video_list = []  # Initialize the video_list attribute as an empty list

    def _update_progress(self, progress):
        """Callback function for updating download progress"""
        # print(f"_update_progress called with: {progress.status}, {progress.percent}, {progress.speed}, {progress.eta}, {progress.filename}, {progress.downloaded_bytes}, {progress.total_bytes}")

        print(f"_update_progress invoked with progress: {progress}")

        if progress and self.current_task:
            # Update UI with progress information
            self.current_task.status = progress.status
            if progress.total_bytes > 0:
                self.current_task.progress = progress.percent

            # Use queue to communicate with main thread
            self.queue.put(
                (
                    "progress",
                    {
                        "status": progress.status,
                        "percent": progress.percent,
                        "speed": progress.speed,
                        "eta": progress.eta,
                        "filename": progress.filename,
                        "downloaded_bytes": progress.downloaded_bytes,
                        "total_bytes": progress.total_bytes,
                    },
                )
            )

    def parse_url(self, url):
        """Parse YouTube URL and return metadata"""
        try:
            return self.downloader.parse_youtube_link(url)
        except Exception as e:
            return {"error": str(e)}

    def download_single_video(self, elements):
        """Download a single video with the elements from UI"""
        url = elements["link_entry"].get()
        quality = elements["quality_menu"].get()
        destination = elements["dest_entry"].get() or os.path.expanduser("~/Downloads")
        cookies = elements["cookies_entry"].get() or None
        custom_args = elements["args_entry"].get() or None

        if not url:
            self._show_error("Please enter a valid URL")
            return

        # Create a UI progress indicator
        progress_frame = self._create_progress_ui(elements.get("download_btn"))

        # Create a download task
        task = DownloadTask(
            task_type="video",
            url=url,
            quality=quality,
            destination=destination,
            cookies=cookies,
            custom_args=custom_args,
        )

        self._start_download_thread(task, progress_frame)

    def download_single_audio(self, elements):
        """Download a single audio file with the elements from UI"""
        url = elements["link_entry"].get()
        quality = elements["quality_menu"].get()
        destination = elements["dest_entry"].get() or os.path.expanduser("~/Downloads")
        cookies = elements["cookies_entry"].get() or None
        custom_args = elements["args_entry"].get() or None

        if not url:
            self._show_error("Please enter a valid URL")
            return

        # Create a UI progress indicator
        progress_frame = self._create_progress_ui(elements.get("download_btn"))

        # Create a download task
        task = DownloadTask(
            task_type="audio",
            url=url,
            quality=quality,
            destination=destination,
            cookies=cookies,
            custom_args=custom_args,
        )

        self._start_download_thread(task, progress_frame)

    def download_clip(self, elements):
        """Download a clip with specified start and end times"""
        url = elements["link_entry"].get()
        quality = elements.get("quality_menu", customtkinter.CTkOptionMenu()).get()
        destination = elements["dest_entry"].get() or os.path.expanduser("~/Downloads")
        cookies = elements["cookies_entry"].get() or None
        custom_args = elements["args_entry"].get() or None

        start_time = elements["start_time_entry"].get() or "00:00:00"
        end_time = elements["end_time_entry"].get() or ""

        if not url:
            self._show_error("Please enter a valid URL")
            return

        # Create a UI progress indicator
        progress_frame = self._create_progress_ui(elements.get("download_btn"))

        # Create a download task
        task = DownloadTask(
            task_type="clip",
            url=url,
            quality=quality,
            destination=destination,
            cookies=cookies,
            custom_args=custom_args,
            start_time=start_time,
            end_time=end_time,
        )

        self._start_download_thread(task, progress_frame)

    def _create_progress_ui(self, parent_widget):
        """Create a progress UI element that replaces the download button"""
        if not parent_widget or not parent_widget.winfo_exists():
            return None

        # Get parent container
        parent = parent_widget.master

        # Hide the download button temporarily
        (
            parent_widget.pack_forget()
            if hasattr(parent_widget, "pack_info")
            else parent_widget.grid_remove()
        )

        # Create a frame with progress bar
        progress_frame = customtkinter.CTkFrame(parent)
        if hasattr(parent_widget, "grid_info"):
            grid_info = parent_widget.grid_info()
            progress_frame.grid(
                row=grid_info["row"],
                column=grid_info["column"],
                columnspan=grid_info.get("columnspan", 1),
                padx=10,
                pady=5,
                sticky="ew",
            )
        else:
            progress_frame.pack(fill="x", padx=10, pady=5)

        # Add progress elements
        progress_label = customtkinter.CTkLabel(
            progress_frame, text="Starting download..."
        )
        progress_label.pack(anchor="w", padx=5, pady=(5, 0))

        progress_bar = customtkinter.CTkProgressBar(progress_frame)
        progress_bar.pack(fill="x", padx=5, pady=5)
        progress_bar.set(0)

        status_label = customtkinter.CTkLabel(progress_frame, text="Preparing...")
        status_label.pack(anchor="w", padx=5, pady=(0, 5))

        # Store widgets in the frame for access later
        progress_frame.progress_label = progress_label
        progress_frame.progress_bar = progress_bar
        progress_frame.status_label = status_label
        progress_frame.original_button = parent_widget

        return progress_frame

    def _start_download_thread(self, task, progress_frame=None):
        """Start a download thread for a single task"""
        with self.lock:
            if self.is_downloading:
                self._show_error("A download is already in progress")
                if progress_frame:
                    self._restore_download_button(progress_frame)
                return

            self.is_downloading = True
            self.current_task = task

            print(f"_start_download_thread called, is_downloading set to: {self.is_downloading}")  # Debugging line

            # Start download thread
            self.thread = Thread(
                target=self._download_worker,
                args=(self.queue, task, progress_frame),
                daemon=True,
            )
            self.thread.start()

            # Start checking queue for updates
            self._check_queue(progress_frame)

    def _download_worker(self, queue, task, progress_frame=None):
        """Background worker that performs the actual download"""
        try:
            if task.task_type == "video":
                success, message = self.downloader.download_video(
                    task.url,
                    task.quality,
                    task.destination,
                    task.cookies,
                    task.custom_args,
                    self.progress_callback,
                )
            elif task.task_type == "audio":
                success, message = self.downloader.download_audio(
                    task.url,
                    task.quality,
                    task.destination,
                    task.cookies,
                    task.custom_args,
                    self.progress_callback,
                )
            elif task.task_type == "clip":
                success, message = self.downloader.download_clip(
                    task.url,
                    task.start_time,
                    task.end_time,
                    task.quality,
                    task.destination,
                    task.cookies,
                    task.custom_args,
                    self.progress_callback,
                )
            else:
                success, message = False, "Unknown task type"

            if success:
                queue.put(("success", {"message": message}))
            else:
                queue.put(("error", {"message": message}))

        except Exception as e:
            queue.put(("error", {"message": str(e)}))
            self.is_downloading = False

    def _check_queue(self, progress_frame=None):
        """Check for messages from worker thread"""
        try:
            msg_type, msg_data = self.queue.get_nowait()

            print(f"_check_queue processing message: {msg_type}, data: {msg_data}")

            if msg_type == "success":
                print("Download completed successfully")
                if progress_frame:
                    self._update_progress_ui(
                        progress_frame, 100, "Download complete", is_done=True
                    )
                    # Restore download button after a short delay
                    self.app.after(
                        2000, lambda: self._restore_download_button(progress_frame)
                    )
                self.is_downloading = False

            elif msg_type == "error":
                print(f"Download failed: {msg_data.get('message')}")
                if progress_frame:
                    self._update_progress_ui(
                        progress_frame,
                        0,
                        f"Error: {msg_data.get('message')}",
                        is_error=True,
                    )
                    # Restore download button after a short delay
                    self.app.after(
                        3000, lambda: self._restore_download_button(progress_frame)
                    )
                self.is_downloading = False

            elif msg_type == "progress":
                if progress_frame:
                    percent = msg_data.get("percent", 0)
                    status = msg_data.get("status", "Downloading...")
                    speed = msg_data.get("speed", 0)
                    eta = msg_data.get("eta", 0)
                    downloaded_bytes = msg_data.get("downloaded_bytes", 0)
                    total_bytes = msg_data.get("total_bytes", 0)

                    # Format bytes for display
                    bytes_text = ""
                    if total_bytes > 0:
                        downloaded_mb = downloaded_bytes / (1024 * 1024)
                        total_mb = total_bytes / (1024 * 1024)
                        bytes_text = f" {downloaded_mb:.1f}/{total_mb:.1f} MB"

                    # Format speed and ETA for display
                    speed_text = f"{self._format_speed(speed)}" if speed else ""
                    eta_text = f", {eta}s remaining" if eta else ""
                    status_text = f"{status}{bytes_text} {speed_text}{eta_text}"

                    self.app.after(0, lambda: self._update_progress_ui(progress_frame, percent, status_text))

        except Empty:
            # Queue is empty, check again after 100ms
            if self.is_downloading:
                print(f"_check_queue called, is_downloading: {self.is_downloading}")
                self.app.after(100, lambda: self._check_queue(progress_frame))

    def _update_progress_ui(
        self, progress_frame, percent, status_text, is_done=False, is_error=False
    ):
        """Update the progress UI with current status"""
        if not progress_frame or not hasattr(progress_frame, "progress_bar"):
            return

        try:
            # Update progress bar
            progress_frame.progress_bar.set(percent / 100)

            # Update status text
            progress_frame.status_label.configure(text=status_text)

            # Update color for completion or error
            if is_done:
                progress_frame.configure(fg_color="green")
                progress_frame.progress_label.configure(text="Download Complete")
            elif is_error:
                progress_frame.configure(fg_color="#B22222")  # Firebrick red
                progress_frame.progress_label.configure(text="Download Failed")

            print(
                f"_update_progress_ui called with percent: {percent}, status_text: {status_text}"
            )
        except Exception as e:
            print(f"Error updating progress UI: {e}")

    def _restore_download_button(self, progress_frame):
        """Restore the original download button after completion"""
        if not progress_frame or not hasattr(progress_frame, "original_button"):
            return

        try:
            button = progress_frame.original_button

            # Destroy progress frame
            progress_frame.destroy()

            # Show original button
            if hasattr(button, "grid_info"):
                button.grid()
            else:
                button.pack()

        except Exception as e:
            print(f"Error restoring download button: {e}")

    def _show_error(self, message):
        """Show error message to user"""
        try:
            import tkinter.messagebox as messagebox

            messagebox.showerror("Download Error", message)
        except:
            print(f"Error: {message}")

    def _format_speed(self, bytes_per_second):
        """Format download speed for display"""
        if bytes_per_second < 1024:
            return f"{bytes_per_second:.0f} B/s"
        elif bytes_per_second < 1024**2:
            return f"{bytes_per_second/1024:.1f} KB/s"
        else:
            return f"{bytes_per_second/(1024**2):.1f} MB/s"

    # Multiple Items Download Functions
    def add_video_to_list(self, elements):
        """Add a video to the download list"""
        url = elements["link_entry"].get()
        if not url:
            self._show_error("Please enter a valid URL")
            return

        # Get video metadata
        metadata = self.parse_url(url)
        if "error" in metadata:
            self._show_error(f"Error parsing URL: {metadata['error']}")
            return

        # Create a task object
        task = DownloadTask(
            task_type="video",
            url=url,
            quality=elements["quality_menu"].get(),
            destination=elements["dest_entry"].get()
            or os.path.expanduser("~/Downloads"),
            cookies=elements["cookies_entry"].get() or None,
            custom_args=elements["args_entry"].get() or None,
            title=metadata.get("title", "Unknown Title"),
            thumbnail=metadata.get("thumbnail", None),
        )

        # Add to our list
        self.video_list.append(task)

        # Update the UI
        self._update_thumbnail_area(
            elements["thumbnail_area"], task, self.video_list.index(task)
        )

        # Clear the URL entry
        elements["link_entry"].delete(0, "end")

    def add_audio_to_list(self, elements):
        """Add an audio item to the download list"""
        url = elements["link_entry"].get()
        if not url:
            self._show_error("Please enter a valid URL")
            return

        # Get video metadata
        metadata = self.parse_url(url)
        if "error" in metadata:
            self._show_error(f"Error parsing URL: {metadata['error']}")
            return

        # Create a task object
        task = DownloadTask(
            task_type="audio",
            url=url,
            quality=elements["quality_menu"].get(),
            destination=elements["dest_entry"].get()
            or os.path.expanduser("~/Downloads"),
            cookies=elements["cookies_entry"].get() or None,
            custom_args=elements["args_entry"].get() or None,
            title=metadata.get("title", "Unknown Title"),
            thumbnail=metadata.get("thumbnail", None),
        )

        # Add to our list
        self.audio_list.append(task)

        # Update the UI
        self._update_thumbnail_area(
            elements["thumbnail_area"], task, self.audio_list.index(task)
        )

        # Clear the URL entry
        elements["link_entry"].delete(0, "end")

    def add_clip_to_list(self, elements):
        """Add a clip to the download list"""
        url = elements["link_entry"].get()
        if not url:
            self._show_error("Please enter a valid URL")
            return

        start_time = elements["start_time_entry"].get() or "00:00:00"
        end_time = elements["end_time_entry"].get() or ""

        # Get video metadata
        metadata = self.parse_url(url)
        if "error" in metadata:
            self._show_error(f"Error parsing URL: {metadata['error']}")
            return

        # Create a task object
        task = DownloadTask(
            task_type="clip",
            url=url,
            quality=elements["quality_menu"].get(),
            destination=elements["dest_entry"].get()
            or os.path.expanduser("~/Downloads"),
            cookies=elements["cookies_entry"].get() or None,
            custom_args=elements["args_entry"].get() or None,
            start_time=start_time,
            end_time=end_time,
            title=metadata.get("title", "Unknown Title"),
            thumbnail=metadata.get("thumbnail", None),
        )

        # Add to our list
        self.clip_list.append(task)

        # Update the UI
        self._update_thumbnail_area(
            elements["thumbnail_area"], task, self.clip_list.index(task)
        )
        # Clear entries
        elements["link_entry"].delete(0, "end")
        elements["start_time_entry"].delete(0, "end")
        if "end_time_entry" in elements:
            elements["end_time_entry"].delete(0, "end")

    def _update_thumbnail_area(self, thumbnail_area, task, index):
        """Update the thumbnail area with a new item"""
        try:
            # Clear placeholder if it's the first item
            if (
                (task.task_type == "video" and len(self.video_list) == 1)
                or (task.task_type == "audio" and len(self.audio_list) == 1)
                or (task.task_type == "clip" and len(self.clip_list) == 1)
            ):
                for widget in thumbnail_area.winfo_children():
                    widget.destroy()

            # Create a frame for this item
            item_frame = customtkinter.CTkFrame(thumbnail_area)
            item_frame.pack(fill="x", padx=10, pady=5, expand=False)

            # Add item information
            title_text = f"{index+1}. {task.title[:40]}"
            if task.task_type == "clip":
                title_text += (
                    f" [{task.start_time}-{task.end_time if task.end_time else 'end'}]"
                )

            title_label = customtkinter.CTkLabel(
                item_frame, text=title_text, wraplength=150
            )
            title_label.pack(anchor="w", padx=5, pady=5)

            # Add thumbnail if available
            if task.thumbnail:
                try:
                    # Download the thumbnail image
                    response = requests.get(task.thumbnail)
                    img_data = response.content

                    # Create PIL image
                    img = Image.open(io.BytesIO(img_data))

                    # Resize to thumbnail size (keeping aspect ratio)
                    width, height = img.size
                    new_height = 45
                    new_width = int(width * (new_height / height))
                    img = img.resize((new_width, new_height), Image.LANCZOS)

                    # Convert to PhotoImage
                    photo_img = ImageTk.PhotoImage(img)

                    # Store reference to prevent garbage collection
                    item_frame.photo_img = photo_img

                    # Create and display thumbnail label
                    thumb_label = customtkinter.CTkLabel(
                        item_frame, text="", image=photo_img
                    )
                    thumb_label.pack(side="left", padx=5, pady=5)
                except Exception as e:
                    print(f"Error loading thumbnail: {e}")
                    # Fallback to text placeholder
                    thumb_placeholder = customtkinter.CTkLabel(
                        item_frame, text="[Thumbnail]", width=80, height=45
                    )
                    thumb_placeholder.pack(side="left", padx=5, pady=5)

            # Add a remove button
            if task.task_type == "video":
                remove_func = lambda: self._remove_from_list(
                    self.video_list, index, item_frame
                )
            elif task.task_type == "audio":
                remove_func = lambda: self._remove_from_list(
                    self.audio_list, index, item_frame
                )
            else:
                remove_func = lambda: self._remove_from_list(
                    self.clip_list, index, item_frame
                )

            remove_btn = customtkinter.CTkButton(
                item_frame, text="Remove", width=60, height=24
            )
            remove_btn.configure(command=remove_func)
            remove_btn.pack(side="right", padx=5, pady=5)

        except Exception as e:
            print(f"Error updating thumbnail area: {e}")

    def _remove_from_list(self, task_list, index, item_frame):
        """Remove an item from the download list"""
        try:
            if 0 <= index < len(task_list):
                task_list.pop(index)
                item_frame.destroy()
                # Re-index remaining items
                # In a complete implementation, this would re-number all visible items
        except Exception as e:
            print(f"Error removing item from list: {e}")

    def download_multi_video(self, elements):
        """Download all videos in the list"""
        if not self.video_list:
            self._show_error("No videos in download list")
            return

        # Create progress UI
        progress_frame = self._create_multi_progress_ui(elements.get("download_btn"))

        # Start the multi-download thread
        self._start_multi_download_thread(self.video_list, progress_frame, "video")

    def download_multi_audio(self, elements):
        """Download all audio files in the list"""
        if not self.audio_list:
            self._show_error("No audio files in download list")
            return

        # Create progress UI
        progress_frame = self._create_multi_progress_ui(elements.get("download_btn"))

        # Start the multi-download thread
        self._start_multi_download_thread(self.audio_list, progress_frame, "audio")

    def download_multi_clip(self, elements):
        """Download all clips in the list"""
        if not self.clip_list:
            self._show_error("No clips in download list")
            return

        # Create progress UI
        progress_frame = self._create_multi_progress_ui(elements.get("download_btn"))

        # Start the multi-download thread
        self._start_multi_download_thread(self.clip_list, progress_frame, "clip")

    def _create_multi_progress_ui(self, parent_widget):
        """Create a progress UI for multi-item downloads"""
        # Similar to _create_progress_ui but with additional information for multiple items
        progress_frame = self._create_progress_ui(parent_widget)

        if progress_frame:
            # Add item counter
            counter_label = customtkinter.CTkLabel(
                progress_frame, text="Downloading item 0/0"
            )
            counter_label.pack(anchor="w", padx=5, pady=(0, 5))
            progress_frame.counter_label = counter_label

        return progress_frame

    def _start_multi_download_thread(self, task_list, progress_frame, list_type):
        """Start a download thread for multiple tasks"""
        with self.lock:
            if self.is_downloading:
                self._show_error("A download is already in progress")
                if progress_frame:
                    self._restore_download_button(progress_frame)
                return

            self.is_downloading = True

            # Start download thread
            self.thread = Thread(
                target=self._multi_download_worker,
                args=(self.queue, task_list.copy(), progress_frame, list_type),
                daemon=True,
            )
            self.thread.start()

            # Start checking queue for updates
            self._check_multi_queue(progress_frame)

    def _multi_download_worker(self, queue, task_list, progress_frame, list_type):
        """Background worker that performs multiple downloads"""
        total_items = len(task_list)
        completed = 0
        failed = 0

        queue.put(
            (
                "multi_progress",
                {
                    "completed": completed,
                    "total": total_items,
                    "failed": failed,
                    "current_item": None,
                },
            )
        )

        for i, task in enumerate(task_list):
            self.current_task = task

            # Update UI with current item
            queue.put(
                (
                    "multi_progress",
                    {
                        "completed": completed,
                        "total": total_items,
                        "failed": failed,
                        "current_item": i + 1,
                        "title": task.title,
                    },
                )
            )

            try:
                if task.task_type == "video":
                    success, message = self.downloader.download_video(
                        task.url,
                        task.quality,
                        task.destination,
                        task.cookies,
                        task.custom_args,
                        self.progress_callback,
                    )
                elif task.task_type == "audio":
                    success, message = self.downloader.download_audio(
                        task.url,
                        task.quality,
                        task.destination,
                        task.cookies,
                        task.custom_args,
                        self.progress_callback,
                    )
                elif task.task_type == "clip":
                    success, message = self.downloader.download_clip(
                        task.url,
                        task.start_time,
                        task.end_time,
                        task.quality,
                        task.destination,
                        task.cookies,
                        task.custom_args,
                        self.progress_callback,
                    )

                if success:
                    completed += 1
                else:
                    failed += 1
                    print(f"Failed to download {task.title}: {message}")

            except Exception as e:
                failed += 1
                print(f"Error downloading {task.title}: {e}")

            # Update progress
            queue.put(
                (
                    "multi_progress",
                    {
                        "completed": completed,
                        "total": total_items,
                        "failed": failed,
                        "current_item": i + 1,
                    },
                )
            )

        # Final update
        if failed == 0:
            queue.put(
                (
                    "multi_success",
                    {"completed": completed, "failed": failed, "total": total_items},
                )
            )
        else:
            queue.put(
                (
                    "multi_partial",
                    {"completed": completed, "failed": failed, "total": total_items},
                )
            )

        # Clear the appropriate list when done
        if list_type == "video":
            self.video_list.clear()
        elif list_type == "audio":
            self.audio_list.clear()
        elif list_type == "clip":
            self.clip_list.clear()

    def _check_multi_queue(self, progress_frame):
        """Check queue for messages from multi-download worker thread"""
        try:
            msg_type, msg_data = self.queue.get_nowait()

            if msg_type == "multi_success":
                completed = msg_data.get("completed", 0)
                total = msg_data.get("total", 0)

                if progress_frame:
                    self._update_progress_ui(
                        progress_frame,
                        100,
                        f"All {completed} items downloaded successfully",
                        is_done=True,
                    )
                    if hasattr(progress_frame, "counter_label"):
                        progress_frame.counter_label.configure(
                            text=f"Completed {completed}/{total}"
                        )

                    # Restore download button after delay
                    self.app.after(
                        3000, lambda: self._restore_download_button(progress_frame)
                    )

                self.is_downloading = False

            elif msg_type == "multi_partial":
                completed = msg_data.get("completed", 0)
                failed = msg_data.get("failed", 0)
                total = msg_data.get("total", 0)

                if progress_frame:
                    self._update_progress_ui(
                        progress_frame,
                        (completed / total) * 100,
                        f"Downloads complete with {failed} failures",
                        is_done=True if failed == 0 else False,
                        is_error=False if failed == 0 else True,
                    )
                    if hasattr(progress_frame, "counter_label"):
                        progress_frame.counter_label.configure(
                            text=f"Completed {completed}/{total} ({failed} failed)"
                        )

                    # Restore download button after delay
                    self.app.after(
                        3000, lambda: self._restore_download_button(progress_frame)
                    )

                self.is_downloading = False

            elif msg_type == "multi_progress":
                if progress_frame:
                    completed = msg_data.get("completed", 0)
                    total = msg_data.get("total", 0)
                    current = msg_data.get("current_item")
                    title = msg_data.get("title", "")

                    # Update progress
                    overall_percent = (completed / total) * 100
                    if current is not None:
                        if title:
                            status_text = f"Downloading {current}/{total}: {title[:30]}"
                        else:
                            status_text = f"Processing item {current}/{total}"

                        if hasattr(progress_frame, "counter_label"):
                            progress_frame.counter_label.configure(
                                text=f"Completed {completed}/{total}"
                            )

                        self._update_progress_ui(
                            progress_frame, overall_percent, status_text
                        )

            elif msg_type in ["progress", "success", "error"]:
                # Handle normal progress updates same as single download
                self._handle_single_progress(msg_type, msg_data, progress_frame)

        except Empty:
            # Queue is empty, check again after 100ms
            if self.is_downloading:
                self.app.after(100, lambda: self._check_multi_queue(progress_frame))

    def _handle_single_progress(self, msg_type, msg_data, progress_frame):
        """Handle single-item progress updates within a multi-download context"""
        if msg_type == "progress" and progress_frame:
            percent = msg_data.get("percent", 0)
            status = msg_data.get("status", "Downloading...")
            speed = msg_data.get("speed", 0)
            downloaded_bytes = msg_data.get("downloaded_bytes", 0)
            total_bytes = msg_data.get("total_bytes", 0)

            # Format bytes for display
            bytes_text = ""
            if total_bytes > 0:
                downloaded_mb = downloaded_bytes / (1024 * 1024)
                total_mb = total_bytes / (1024 * 1024)
                bytes_text = f" {downloaded_mb:.1f}/{total_mb:.1f} MB"

            # Format speed for display
            speed_text = f"{self._format_speed(speed)}" if speed else ""
            status_text = f"{status}{bytes_text} {speed_text}"

            # For multi-downloads, we don't update the overall progress here,
            # just show the current file's status
            if hasattr(progress_frame, "status_label"):
                progress_frame.status_label.configure(text=status_text)
