import customtkinter
from src.utils.download_manager import DownloadManager
import os
from pathlib import Path

# Import all screen modules
from src.ui.single_video_screen import SingleVideoScreen
from src.ui.multi_video_screen import MultiVideoScreen
from src.ui.single_clip_screen import SingleClipScreen 
from src.ui.multi_clip_screen import MultiClipScreen
from src.ui.single_audio_screen import SingleAudioScreen
from src.ui.multi_audio_screen import MultiAudioScreen

customtkinter.set_appearance_mode("system")

class App(customtkinter.CTk):
    def __init__(self):
        # Initialize default directories first
        self.default_video_dir = self.get_default_directory("Videos")
        self.default_music_dir = self.get_default_directory("Music")

        # Call the parent class initializer
        super().__init__()
        
        self.title("GUI Youtube-dl")
        self.geometry("900x700") # Increased size for better spacing with new styles
        self.downloader = DownloadManager(self)

        # Initialize all screen objects
        self.single_video_screen = SingleVideoScreen(self)
        self.multi_video_screen = MultiVideoScreen(self)
        self.single_clip_screen = SingleClipScreen(self)
        self.multi_clip_screen = MultiClipScreen(self)
        self.single_audio_screen = SingleAudioScreen(self)
        self.multi_audio_screen = MultiAudioScreen(self)

        self.tabview = customtkinter.CTkTabview(master=self, corner_radius=8)
        self.tabview.pack(padx=20, pady=20, expand=True, fill="both") # Increased pady for main tabview

        # Add tabs for each function
        tab_names = ["Single Video", "Multiple Videos", "Single Clip", "Multiple Clips", 
                     "Single Audio", "Multiple Audio"]
        for name in tab_names:
            self.tabview.add(name)        # Setup UI for each tab using the dedicated screen classes
        self.setup_tabs()
        

    def get_default_directory(self, folder_name):
        """Get the default directory for videos or music based on the OS."""
        return str(Path.home() / folder_name)

    def prepopulate_download_directory(self):
        """Prepopulate the destination field in the UI for all tabs."""
        if self.single_video_elements:
            self.single_video_elements["dest_entry"].insert(0, self.default_video_dir)
        if self.multi_video_elements:
            self.multi_video_elements["dest_entry"].insert(0, self.default_video_dir)
        if self.single_audio_elements:
            self.single_audio_elements["dest_entry"].insert(0, self.default_music_dir)
        if self.multi_audio_elements:
            self.multi_audio_elements["dest_entry"].insert(0, self.default_video_dir)
        if self.multi_clip_elements:
            self.multi_clip_elements["dest_entry"].insert(0, self.default_video_dir)
        if self.single_clip_elements:
            self.single_clip_elements["dest_entry"].insert(0, self.default_video_dir)

    def fetch_metadata_and_update_quality(self, link_entry, quality_dropdown):
        """Fetch metadata for the given link and update the quality dropdown."""
        link = link_entry.get()
        if not link:
            return

        # Disable the dropdown while fetching metadata
        quality_dropdown.configure(state="disabled")
        quality_dropdown.set("Fetching...")

        # Fetch metadata
        metadata = self.downloader.parse_url(link)
        if "error" in metadata:
            quality_dropdown.set("Error fetching metadata")
            return

        # Extract available qualities
        qualities = [fmt["format_note"] for fmt in metadata.get("formats", []) if fmt.get("format_note")]
        qualities = list(set(qualities))  # Remove duplicates

        # Update the dropdown
        quality_dropdown.configure(values=qualities, state="normal")
        if qualities:
            quality_dropdown.set(qualities[0])
        else:
            quality_dropdown.set("No qualities available")

    def setup_tabs(self):
        """Initialize all tab UIs using their respective screen classes."""
        self.single_video_elements = self.single_video_screen.setup_ui(self.tabview.tab("Single Video"))
        self.multi_video_elements = self.multi_video_screen.setup_ui(self.tabview.tab("Multiple Videos"))
        self.single_clip_elements = self.single_clip_screen.setup_ui(self.tabview.tab("Single Clip"))
        self.multi_clip_elements = self.multi_clip_screen.setup_ui(self.tabview.tab("Multiple Clips"))
        self.single_audio_elements = self.single_audio_screen.setup_ui(self.tabview.tab("Single Audio"))
        self.multi_audio_elements = self.multi_audio_screen.setup_ui(self.tabview.tab("Multiple Audio"))

        # Bind link entry to fetch metadata and update quality dropdown
        if self.single_video_elements:
            link_entry = self.single_video_elements["link_entry"]
            quality_dropdown = self.single_video_elements["quality_menu"]
            link_entry.bind("<FocusOut>", lambda e: self.fetch_metadata_and_update_quality(link_entry, quality_dropdown))

        self.prepopulate_download_directory()


    # Removed create_tab_content as it's replaced by specific setup methods
    # ... placeholder methods for future tab-specific functionalities ...

if __name__ == "__main__":
    app = App()
    app.mainloop()