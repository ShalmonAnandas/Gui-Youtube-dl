import customtkinter
from src.ui.base_screen import BaseScreen

class MultiVideoScreen(BaseScreen):
    """Screen for downloading multiple videos."""
    
    def __init__(self, app):
        super().__init__(app)
        
    def setup_ui(self, tab_frame):
        """Set up UI elements for the multiple videos tab."""
        elements = self._setup_multi_common_ui(tab_frame, item_type="Video")
        
        # Connect download button to functionality
        elements["download_btn"].configure(command=lambda: self.app.downloader.download_multi_video(elements))
        elements["add_button"].configure(command=lambda: self.app.downloader.add_video_to_list(elements))
        
        return elements
    
    def add_video_to_list(self, elements):
        """Add a video to the download list."""
        self.app.downloader.add_video_to_list(elements)
