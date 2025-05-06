import customtkinter
from src.ui.base_screen import BaseScreen

class SingleClipScreen(BaseScreen):
    """Screen for downloading a single clip from a video."""
    
    def __init__(self, app):
        super().__init__(app)
        
    def setup_ui(self, tab_frame):
        """Set up UI elements for the single clip tab."""
        elements = self._create_common_ui_elements(tab_frame, has_start_time=True, has_end_time=True)
        
        # Connect download button to functionality
        elements["download_btn"].configure(command=lambda: self.app.downloader.download_clip(elements))
        
        return elements
