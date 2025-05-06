import customtkinter

class DownloadManagerUI:
    def __init__(self, app):
        self.app = app

    def create_progress_ui(self, parent_widget):
        """Create a progress UI element that replaces the download button."""
        if not parent_widget or not parent_widget.winfo_exists():
            return None
        parent = parent_widget.master
        parent_widget.pack_forget() if hasattr(parent_widget, 'pack_info') else parent_widget.grid_remove()
        progress_frame = customtkinter.CTkFrame(parent)
        if hasattr(parent_widget, 'grid_info'):
            grid_info = parent_widget.grid_info()
            progress_frame.grid(row=grid_info['row'], column=grid_info['column'], 
                                columnspan=grid_info.get('columnspan', 1), 
                                padx=10, pady=5, sticky="ew")
        else:
            progress_frame.pack(fill="x", padx=10, pady=5)
        progress_label = customtkinter.CTkLabel(progress_frame, text="Starting download...")
        progress_label.pack(anchor="w", padx=5, pady=(5, 0))
        progress_bar = customtkinter.CTkProgressBar(progress_frame)
        progress_bar.pack(fill="x", padx=5, pady=5)
        progress_bar.set(0)
        status_label = customtkinter.CTkLabel(progress_frame, text="Preparing...")
        status_label.pack(anchor="w", padx=5, pady=(0, 5))
        progress_frame.progress_label = progress_label
        progress_frame.progress_bar = progress_bar
        progress_frame.status_label = status_label
        progress_frame.original_button = parent_widget
        return progress_frame

    def restore_download_button(self, progress_frame):
        """Restore the original download button after completion."""
        if not progress_frame or not hasattr(progress_frame, "original_button"):
            return
        try:
            button = progress_frame.original_button
            progress_frame.destroy()
            if hasattr(button, 'grid_info'):
                button.grid()
            else:
                button.pack()
        except Exception as e:
            print(f"Error restoring download button: {e}")
