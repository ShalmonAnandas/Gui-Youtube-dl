import customtkinter
from customtkinter import filedialog

class BaseScreen:
    """Base class with common UI components and utilities for all screens."""
    
    def __init__(self, app):
        self.app = app
        
    def _create_common_ui_elements(self, parent_frame, has_quality=True, has_start_time=False, has_end_time=False):
        """Helper to create common UI elements for download tabs with enhanced styling."""
        elements = {}
        
        # Main container frame for this set of controls for better padding
        container = customtkinter.CTkFrame(parent_frame, fg_color="transparent")
        container.pack(expand=True, fill="both", padx=15, pady=15)

        row_idx = 0
        label_font = ("Roboto", 14)
        widget_corner_radius = 8
        default_pady = (5, 7) # pady for most rows
        button_pady = (15, 7) # pady for download button

        # Link
        customtkinter.CTkLabel(container, text="Link:", font=label_font).grid(row=row_idx, column=0, padx=10, pady=default_pady, sticky="w")
        elements["link_entry"] = customtkinter.CTkEntry(container, width=350, corner_radius=widget_corner_radius)
        elements["link_entry"].grid(row=row_idx, column=1, columnspan=2, padx=10, pady=default_pady, sticky="ew")
        row_idx += 1

        if has_quality:
            # Quality
            customtkinter.CTkLabel(container, text="Quality:", font=label_font).grid(row=row_idx, column=0, padx=10, pady=default_pady, sticky="w")
            qualities = ["Best", "2160p (4K)", "1440p (2K)", "1080p (FHD)", "720p (HD)", "480p", "360p", "Audio Only"] 
            elements["quality_menu"] = customtkinter.CTkOptionMenu(container, values=qualities, corner_radius=widget_corner_radius)
            elements["quality_menu"].grid(row=row_idx, column=1, columnspan=2, padx=10, pady=default_pady, sticky="ew")
            row_idx += 1
        
        if has_start_time:
            # Start Time
            customtkinter.CTkLabel(container, text="Start Time (HH:MM:SS):", font=label_font).grid(row=row_idx, column=0, padx=10, pady=default_pady, sticky="w")
            elements["start_time_entry"] = customtkinter.CTkEntry(container, corner_radius=widget_corner_radius)
            elements["start_time_entry"].grid(row=row_idx, column=1, columnspan=2, padx=10, pady=default_pady, sticky="ew")
            row_idx += 1

        if has_end_time:
            # End Time
            customtkinter.CTkLabel(container, text="End Time (HH:MM:SS):", font=label_font).grid(row=row_idx, column=0, padx=10, pady=default_pady, sticky="w")
            elements["end_time_entry"] = customtkinter.CTkEntry(container, corner_radius=widget_corner_radius)
            elements["end_time_entry"].grid(row=row_idx, column=1, columnspan=2, padx=10, pady=default_pady, sticky="ew")
            row_idx += 1

        # Download Destination
        customtkinter.CTkLabel(container, text="Destination:", font=label_font).grid(row=row_idx, column=0, padx=10, pady=default_pady, sticky="w")
        elements["dest_entry"] = customtkinter.CTkEntry(container, width=300, corner_radius=widget_corner_radius)
        elements["dest_entry"].grid(row=row_idx, column=1, padx=10, pady=default_pady, sticky="ew")
        elements["dest_browse_btn"] = customtkinter.CTkButton(container, text="Browse", width=80, corner_radius=widget_corner_radius, command=lambda: self._browse_folder(elements["dest_entry"]))
        elements["dest_browse_btn"].grid(row=row_idx, column=2, padx=(5,10), pady=default_pady)
        row_idx += 1

        # Cookies File
        customtkinter.CTkLabel(container, text="Cookies File:", font=label_font).grid(row=row_idx, column=0, padx=10, pady=default_pady, sticky="w")
        elements["cookies_entry"] = customtkinter.CTkEntry(container, width=300, corner_radius=widget_corner_radius)
        elements["cookies_entry"].grid(row=row_idx, column=1, padx=10, pady=default_pady, sticky="ew")
        elements["cookies_browse_btn"] = customtkinter.CTkButton(container, text="Browse", width=80, corner_radius=widget_corner_radius, command=lambda: self._browse_file(elements["cookies_entry"]))
        elements["cookies_browse_btn"].grid(row=row_idx, column=2, padx=(5,10), pady=default_pady)
        row_idx += 1
        
        # Custom Args
        customtkinter.CTkLabel(container, text="Custom Args:", font=label_font).grid(row=row_idx, column=0, padx=10, pady=default_pady, sticky="w")
        elements["args_entry"] = customtkinter.CTkEntry(container, corner_radius=widget_corner_radius)
        elements["args_entry"].grid(row=row_idx, column=1, columnspan=2, padx=10, pady=default_pady, sticky="ew")
        row_idx += 1

        # Download Button
        elements["download_btn"] = customtkinter.CTkButton(container, text="Download", corner_radius=widget_corner_radius, height=35)
        elements["download_btn"].grid(row=row_idx, column=0, columnspan=3, padx=10, pady=button_pady, sticky="ew")
        
        container.columnconfigure(1, weight=1) # Allow middle column with entry to expand
        return elements

    def _setup_multi_common_ui(self, tab_frame, item_type="Video"):
        """Common UI setup for multiple items download screens."""
        main_frame = customtkinter.CTkFrame(tab_frame, fg_color="transparent")
        main_frame.pack(expand=True, fill="both", padx=5, pady=5)
        main_frame.grid_columnconfigure(0, weight=3) # Left part takes more space
        main_frame.grid_columnconfigure(1, weight=2) # Right part for thumbnails
        main_frame.grid_rowconfigure(0, weight=1)

        left_frame = customtkinter.CTkFrame(main_frame, corner_radius=8)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=(10,5), pady=10)
        left_frame.grid_columnconfigure(1, weight=1) # Allow entry fields to expand
        
        label_font = ("Roboto", 14)
        widget_corner_radius = 8
        default_pady = (5, 7)
        button_pady = (15, 7)
        row_idx = 0

        # Link entry and Add button
        customtkinter.CTkLabel(left_frame, text="Link:", font=label_font).grid(row=row_idx, column=0, padx=10, pady=default_pady, sticky="w")
        link_entry = customtkinter.CTkEntry(left_frame, width=280, corner_radius=widget_corner_radius)
        link_entry.grid(row=row_idx, column=1, padx=10, pady=default_pady, sticky="ew")
        add_button = customtkinter.CTkButton(left_frame, text="Add", width=60, corner_radius=widget_corner_radius) 
        add_button.grid(row=row_idx, column=2, padx=(5,10), pady=default_pady)
        row_idx += 1

        # Quality (below link paste)
        customtkinter.CTkLabel(left_frame, text="Quality:", font=label_font).grid(row=row_idx, column=0, padx=10, pady=default_pady, sticky="w")
        video_qualities = ["Best", "1080p", "720p", "480p", "Audio Only"]
        audio_qualities = ["Best Audio", "mp3", "m4a", "opus", "aac"]
        qualities = video_qualities if item_type != "Audio" else audio_qualities
        quality_menu = customtkinter.CTkOptionMenu(left_frame, values=qualities, corner_radius=widget_corner_radius)
        quality_menu.grid(row=row_idx, column=1, columnspan=2, padx=10, pady=default_pady, sticky="ew")
        row_idx += 1
        
        # Download Destination
        customtkinter.CTkLabel(left_frame, text="Destination:", font=label_font).grid(row=row_idx, column=0, padx=10, pady=default_pady, sticky="w")
        dest_entry = customtkinter.CTkEntry(left_frame, width=230, corner_radius=widget_corner_radius)
        dest_entry.grid(row=row_idx, column=1, padx=10, pady=default_pady, sticky="ew")
        dest_browse_btn = customtkinter.CTkButton(left_frame, text="Browse", width=60, corner_radius=widget_corner_radius, command=lambda: self._browse_folder(dest_entry))
        dest_browse_btn.grid(row=row_idx, column=2, padx=(5,10), pady=default_pady)
        row_idx += 1

        # Cookies File
        customtkinter.CTkLabel(left_frame, text="Cookies File:", font=label_font).grid(row=row_idx, column=0, padx=10, pady=default_pady, sticky="w")
        cookies_entry = customtkinter.CTkEntry(left_frame, width=230, corner_radius=widget_corner_radius)
        cookies_entry.grid(row=row_idx, column=1, padx=10, pady=default_pady, sticky="ew")
        cookies_browse_btn = customtkinter.CTkButton(left_frame, text="Browse", width=60, corner_radius=widget_corner_radius, command=lambda: self._browse_file(cookies_entry))
        cookies_browse_btn.grid(row=row_idx, column=2, padx=(5,10), pady=default_pady)
        row_idx += 1
        
        # Custom Args
        customtkinter.CTkLabel(left_frame, text="Custom Args:", font=label_font).grid(row=row_idx, column=0, padx=10, pady=default_pady, sticky="w")
        args_entry = customtkinter.CTkEntry(left_frame, corner_radius=widget_corner_radius)
        args_entry.grid(row=row_idx, column=1, columnspan=2, padx=10, pady=default_pady, sticky="ew")
        row_idx += 1

        # Download Button
        download_btn = customtkinter.CTkButton(left_frame, text=f"Download All {item_type}s", corner_radius=widget_corner_radius, height=35)
        download_btn.grid(row=row_idx, column=0, columnspan=3, padx=10, pady=button_pady, sticky="ew")

        # Right frame for thumbnails
        right_frame = customtkinter.CTkScrollableFrame(main_frame, label_text=f"Added {item_type}s", label_font=("Roboto", 14, "bold"), corner_radius=8)
        right_frame.grid(row=0, column=1, sticky="nsew", padx=(5,10), pady=10)
        # Placeholder - replace with actual thumbnail display logic
        placeholder_label = customtkinter.CTkLabel(right_frame, text=f"Added {item_type}s will appear here.", font=("Roboto", 12), text_color="gray60")
        placeholder_label.pack(padx=20, pady=20, expand=True)
        
        return {"link_entry": link_entry, "add_button": add_button, "quality_menu": quality_menu, 
                "dest_entry": dest_entry, "cookies_entry": cookies_entry, "args_entry": args_entry, 
                "download_btn": download_btn, "thumbnail_area": right_frame}
                
    def _browse_folder(self, entry_widget):
        """Open file dialog to select a folder and update the entry widget."""
        filepath = filedialog.askdirectory()
        if filepath:
            entry_widget.delete(0, "end")
            entry_widget.insert(0, filepath)

    def _browse_file(self, entry_widget):
        """Open file dialog to select a file and update the entry widget."""
        filepath = filedialog.askopenfilename()
        if filepath:
            entry_widget.delete(0, "end")
            entry_widget.insert(0, filepath)
