from threading import Thread, Lock
import time
import os
import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
import requests
import io

from src.models.download_task import DownloadTask
from src.utils.download_manager_ui import DownloadManagerUI
from src.utils.downloader import Downloader


class DownloadManager:
    def __init__(self, app):
        self.app = app
        self.downloader = Downloader()
        self.ui = DownloadManagerUI(app)
        self.lock = Lock()  # Initialize a threading lock
        self.is_downloading = False  # Initialize the is_downloading flag
        self.current_task = None  # Initialize the current_task attribute
        self.video_list = []  # Initialize the video_list attribute as an empty list
        self.audio_list = []  # Initialize the audio_list attribute as an empty list
        self.clip_list = []  # Initialize the clip_list attribute as an empty list

    def _update_progress(self, progress):
        """Legacy callback function - no longer used with direct UI updates"""
        pass

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

        # Store grid info before hiding the button
        grid_info = None
        if hasattr(parent_widget, "grid_info") and parent_widget.grid_info():
            grid_info = parent_widget.grid_info().copy()

        # Hide the download button temporarily
        if grid_info:
            parent_widget.grid_remove()
        else:
            parent_widget.pack_forget()

        # Create a frame with progress bar
        progress_frame = customtkinter.CTkFrame(parent)
        if grid_info:
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
        progress_frame.grid_info_backup = grid_info

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

            # Start download thread
            self.thread = Thread(
                target=self._download_worker,
                args=(task, progress_frame),
                daemon=True,
            )
            self.thread.start()

    def _download_worker(self, task, progress_frame=None):
        """Background worker that performs the actual download"""
        try:
            if task.task_type == "video":
                success, message = self.downloader.download_video(
                    task.url,
                    task.quality,
                    task.destination,
                    task.cookies,
                    task.custom_args,
                    progress_frame,
                    self.app,
                )
            elif task.task_type == "audio":
                success, message = self.downloader.download_audio(
                    task.url,
                    task.quality,
                    task.destination,
                    task.cookies,
                    task.custom_args,
                    progress_frame,
                    self.app,
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
                    progress_frame,
                    self.app,
                )
            else:
                success, message = False, "Unknown task type"

            # Handle completion directly
            def handle_completion():
                if success:
                    if progress_frame:
                        self._update_progress_ui(
                            progress_frame, 100, "Download complete", is_done=True
                        )
                        # Restore download button after delay
                        def restore_button():
                            self._restore_download_button(progress_frame)
                        self.app.after(2000, restore_button)
                else:
                    if progress_frame:
                        self._update_progress_ui(
                            progress_frame,
                            0,
                            f"Error: {message}",
                            is_error=True,
                        )
                        # Restore download button after delay
                        def restore_button():
                            self._restore_download_button(progress_frame)
                        self.app.after(3000, restore_button)

            # Schedule completion handling on main thread
            self.app.after(0, handle_completion)

        except Exception as e:
            def handle_error():
                if progress_frame:
                    self._update_progress_ui(
                        progress_frame,
                        0,
                        f"Error: {str(e)}",
                        is_error=True,
                    )
                    def restore_button():
                        self._restore_download_button(progress_frame)
                    self.app.after(3000, restore_button)
            
            self.app.after(0, handle_error)
        finally:
            # Always reset downloading flag when worker finishes
            self.is_downloading = False

    def _update_progress_ui(
        self, progress_frame, percent, status_text, is_done=False, is_error=False
    ):
        """Update the progress UI with current status"""
        if not progress_frame or not hasattr(progress_frame, "progress_bar"):
            return

        try:
            # Ensure percent is within valid range
            percent = max(0, min(100, percent))

            # Update progress bar
            progress_frame.progress_bar.set(percent / 100)

            # Update status text
            if hasattr(progress_frame, "status_label"):
                progress_frame.status_label.configure(text=status_text)

            # Update color for completion or error
            if is_done:
                progress_frame.configure(fg_color="green")
                if hasattr(progress_frame, "progress_label"):
                    progress_frame.progress_label.configure(text="Download Complete")
            elif is_error:
                progress_frame.configure(fg_color="#B22222")  # Firebrick red
                if hasattr(progress_frame, "progress_label"):
                    progress_frame.progress_label.configure(text="Download Failed")

        except Exception as e:
            pass  # Silently handle UI update errors

    def _restore_download_button(self, progress_frame):
        """Restore the original download button after completion"""
        if not progress_frame or not hasattr(progress_frame, "original_button"):
            return

        try:
            button = progress_frame.original_button
            grid_info = getattr(progress_frame, "grid_info_backup", None)

            # Destroy progress frame
            progress_frame.destroy()

            # Show original button
            if grid_info:
                button.grid(**grid_info)
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
                args=(task_list.copy(), progress_frame, list_type),
                daemon=True,
            )
            self.thread.start()

    def _multi_download_worker(self, task_list, progress_frame, list_type):
        """Background worker that performs multiple downloads"""
        total_items = len(task_list)
        completed = 0
        failed = 0

        try:
            for i, task in enumerate(task_list):
                self.current_task = task

                # Update UI with current item
                def update_current_item():
                    if progress_frame and hasattr(progress_frame, "counter_label"):
                        progress_frame.counter_label.configure(
                            text=f"Downloading {i + 1}/{total_items}: {task.title[:30] if task.title else 'Unknown'}"
                        )
                
                self.app.after(0, update_current_item)

                try:
                    if task.task_type == "video":
                        success, message = self.downloader.download_video(
                            task.url,
                            task.quality,
                            task.destination,
                            task.cookies,
                            task.custom_args,
                            progress_frame,
                            self.app,
                        )
                    elif task.task_type == "audio":
                        success, message = self.downloader.download_audio(
                            task.url,
                            task.quality,
                            task.destination,
                            task.cookies,
                            task.custom_args,
                            progress_frame,
                            self.app,
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
                            progress_frame,
                            self.app,
                        )

                    if success:
                        completed += 1
                    else:
                        failed += 1

                except Exception as e:
                    failed += 1

            # Final update
            def final_update():
                if progress_frame:
                    if failed == 0:
                        self._update_progress_ui(
                            progress_frame,
                            100,
                            f"All {completed} items downloaded successfully",
                            is_done=True,
                        )
                    else:
                        self._update_progress_ui(
                            progress_frame,
                            (completed / total_items) * 100,
                            f"Downloads complete: {completed} successful, {failed} failed",
                            is_done=True,
                            is_error=failed > 0,
                        )
                    
                    if hasattr(progress_frame, "counter_label"):
                        progress_frame.counter_label.configure(
                            text=f"Completed {completed}/{total_items}" + (f" ({failed} failed)" if failed > 0 else "")
                        )

                    # Restore download button after delay
                    def restore_button():
                        self._restore_download_button(progress_frame)

                    self.app.after(3000, restore_button)

            self.app.after(0, final_update)

        finally:
            # Clear the appropriate list when done
            if list_type == "video":
                self.video_list.clear()
            elif list_type == "audio":
                self.audio_list.clear()
            elif list_type == "clip":
                self.clip_list.clear()
            
            self.is_downloading = False


