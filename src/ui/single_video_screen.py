import customtkinter
from src.ui.base_screen import BaseScreen

class SingleVideoScreen(BaseScreen):
    """Screen for downloading a single video."""
    
    def __init__(self, app):
        super().__init__(app)
        
    def setup_ui(self, tab_frame):
        """Set up UI elements for the single video tab."""
        elements = self._create_common_ui_elements(tab_frame)
        # You can add video-specific UI customization here if needed
        
        # Connect download button to functionality
        elements["download_btn"].configure(command=lambda: self.app.downloader.download_single_video(elements))
        
        return elements
