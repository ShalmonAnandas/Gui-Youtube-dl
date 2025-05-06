from threading import Thread, Lock
from queue import Queue, Empty
from src.models.download_task import DownloadTask

class DownloadManagerCore:
    def __init__(self, downloader, progress_callback):
        self.is_downloading = False
        self.lock = Lock()
        self.thread = None
        self.queue = Queue()
        self.downloader = downloader
        self.progress_callback = progress_callback
        self.current_task = None

    def start_download_thread(self, task):
        """Start a download thread for a single task."""
        with self.lock:
            if self.is_downloading:
                raise RuntimeError("A download is already in progress")
            self.is_downloading = True
            self.current_task = task
            self.thread = Thread(target=self._download_worker, args=(task,), daemon=True)
            self.thread.start()

    def _download_worker(self, task):
        """Background worker that performs the actual download."""
        try:
            if task.task_type == "video":
                success, message = self.downloader.download_video(
                    task.url, task.quality, task.destination, 
                    task.cookies, task.custom_args, self.progress_callback
                )
            elif task.task_type == "audio":
                success, message = self.downloader.download_audio(
                    task.url, task.quality, task.destination, 
                    task.cookies, task.custom_args, self.progress_callback
                )
            elif task.task_type == "clip":
                success, message = self.downloader.download_clip(
                    task.url, task.start_time, task.end_time, task.quality,
                    task.destination, task.cookies, task.custom_args, self.progress_callback
                )
            else:
                success, message = False, "Unknown task type"
            self.queue.put(("success" if success else "error", {"message": message}))
        except Exception as e:
            self.queue.put(("error", {"message": str(e)}))
        finally:
            self.is_downloading = False
