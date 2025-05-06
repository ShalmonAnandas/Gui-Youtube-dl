import customtkinter
from src.ui.base_screen import BaseScreen

class SingleAudioScreen(BaseScreen):
    """Screen for downloading a single audio file."""
    
    def __init__(self, app):
        super().__init__(app)
        
    def setup_ui(self, tab_frame):
        """Set up UI elements for the single audio tab."""
        elements = self._create_common_ui_elements(tab_frame, has_quality=True)
        
        # Customize audio quality options
        audio_qualities = ["Best Audio", "320k", "256k", "192k", "128k", "opus", "aac", "vorbis", "mp3", "m4a"]
        elements["quality_menu"].configure(values=audio_qualities)
        elements["quality_menu"].set("Best Audio")
        
        # Connect download button to functionality
        elements["download_btn"].configure(command=lambda: self.app.downloader.download_single_audio(elements))
        
        return elements
