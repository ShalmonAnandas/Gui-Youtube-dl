import customtkinter
from src.ui.base_screen import BaseScreen

class MultiAudioScreen(BaseScreen):
    """Screen for downloading multiple audio files."""
    
    def __init__(self, app):
        super().__init__(app)
        
    def setup_ui(self, tab_frame):
        """Set up UI elements for the multiple audio tab."""
        elements = self._setup_multi_common_ui(tab_frame, item_type="Audio")
        
        # Connect buttons to functionality
        elements["add_button"].configure(command=lambda: self.app.downloader.add_audio_to_list(elements))
        elements["download_btn"].configure(command=lambda: self.app.downloader.download_multi_audio(elements))
        
        return elements
    
    def add_audio_to_list(self, elements):
        """Add an audio file to the download list."""
        self.app.downloader.add_audio_to_list(elements)
