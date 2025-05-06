class DownloadTask:
    def __init__(self, task_type, url, quality, destination, cookies=None, custom_args=None, **kwargs):
        self.task_type = task_type  # 'video', 'audio', or 'clip'
        self.url = url
        self.quality = quality
        self.destination = destination
        self.cookies = cookies
        self.custom_args = custom_args
        
        # For clips
        self.start_time = kwargs.get('start_time', None)
        self.end_time = kwargs.get('end_time', None)
        
        # Task metadata
        self.title = kwargs.get('title', 'Unknown Title')
        self.thumbnail = kwargs.get('thumbnail', None)
        self.status = 'Queued'
        self.progress = 0
