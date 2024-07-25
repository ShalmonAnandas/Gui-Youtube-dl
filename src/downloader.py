from main import TestDownload
import threading


class Downloader:
    def __init__(self, app):
        self.app = app
        self.isDownloading = True
        self.counter = 1
        self.thread = None

    def start_download(self):
        self.thread = threading.Thread(target=TestDownload)
        self.thread.start()
        self.isDownloading = False
        self.check_thread()

    def check_thread(self):
        if self.thread.is_alive():
            self.app.after(100, self.check_thread)
        else:
            self.thread.join()
            self.isDownloading = True
            print("Download completed and thread joined.")

    def button_function(self):
        if self.isDownloading:
            self.start_download()
        print(f"button pressed {self.counter}")
        self.counter += 1
