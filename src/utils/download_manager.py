from threading import Thread
from queue import Queue, Empty
import time

from src.utils.downloader import Downloader

class DownloadManager:
    def __init__(self, app):
        self.app = app
        self.is_downloading = False
        self.counter = 1
        self.thread = None
        self.queue = Queue()
        
    def start_download(self):
        if self.is_downloading:
            print("Download already in progress")
            return
            
        self.is_downloading = True
        # Create thread with args
        self.thread = Thread(
            target=self.download_worker,
            args=(self.queue,),
            daemon=True  # Make thread daemon so it closes with main app
        )
        self.thread.start() 
        
        # Start checking the queue
        self.check_queue()
        
    def download_worker(self, queue):
        try:
            # Your actual download code here
            Downloader("bestaudio+602")
            queue.put(("success", None))
        except Exception as e:
            queue.put(("error", str(e)))
            
    def check_queue(self):
        try:
            msg_type, msg_data = self.queue.get_nowait()
            
            if msg_type == "success":
                print("Download completed successfully")
                self.is_downloading = False
            elif msg_type == "error":
                print(f"Download failed: {msg_data}")
                self.is_downloading = False
            
        except Empty:
            # Queue is empty, check again after 100ms
            self.app.after(100, self.check_queue)
            
    def button_function(self):
        self.start_download()
        print(f"Button pressed {self.counter}")
        self.counter += 1