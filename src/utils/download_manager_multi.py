from threading import Thread
from queue import Empty, Queue


class DownloadManagerMulti:
    def __init__(self, downloader, progress_callback):
        self.downloader = downloader
        self.progress_callback = progress_callback
        self.is_downloading = False
        self.queue = None

    def start_multi_download_thread(self, task_list, progress_frame, list_type):
        """Start a download thread for multiple tasks."""
        if self.is_downloading:
            raise RuntimeError("A download is already in progress")
        self.is_downloading = True
        self.queue = Queue()
        thread = Thread(
            target=self._multi_download_worker,
            args=(task_list, progress_frame, list_type),
            daemon=True,
        )
        thread.start()

    def _multi_download_worker(self, task_list, progress_frame, list_type):
        """Background worker that performs multiple downloads."""
        # ...existing code for multi-download logic...
