import customtkinter
from src.ui.base_screen import BaseScreen

class MultiClipScreen(BaseScreen):
    """Screen for downloading multiple clips."""
    
    def __init__(self, app):
        super().__init__(app)
        
    def setup_ui(self, tab_frame):
        """Set up UI elements for the multiple clips tab."""
        main_frame = customtkinter.CTkFrame(tab_frame, fg_color="transparent")
        main_frame.pack(expand=True, fill="both", padx=5, pady=5)
        main_frame.grid_columnconfigure(0, weight=3) 
        main_frame.grid_columnconfigure(1, weight=2) 
        main_frame.grid_rowconfigure(0, weight=1)

        left_frame = customtkinter.CTkFrame(main_frame, corner_radius=8)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=(10,5), pady=10)
        left_frame.grid_columnconfigure(1, weight=1)
        
        label_font = ("Roboto", 14)
        widget_corner_radius = 8
        default_pady = (5, 7)
        button_pady = (15, 7)
        row_idx = 0
        
        # Link entry
        customtkinter.CTkLabel(left_frame, text="Link:", font=label_font).grid(row=row_idx, column=0, padx=10, pady=default_pady, sticky="w")
        link_entry = customtkinter.CTkEntry(left_frame, width=250, corner_radius=widget_corner_radius)
        link_entry.grid(row=row_idx, column=1, columnspan=2, padx=10, pady=default_pady, sticky="ew")
        row_idx += 1

        # Start Time (for the clip to be added)
        customtkinter.CTkLabel(left_frame, text="Start (HH:MM:SS):", font=label_font).grid(row=row_idx, column=0, padx=10, pady=default_pady, sticky="w")
        start_time_entry = customtkinter.CTkEntry(left_frame, corner_radius=widget_corner_radius)
        start_time_entry.grid(row=row_idx, column=1, columnspan=2, padx=10, pady=default_pady, sticky="ew")
        row_idx += 1
        
        # End Time (for the clip to be added)
        customtkinter.CTkLabel(left_frame, text="End (HH:MM:SS):", font=label_font).grid(row=row_idx, column=0, padx=10, pady=default_pady, sticky="w")
        end_time_entry = customtkinter.CTkEntry(left_frame, corner_radius=widget_corner_radius)
        end_time_entry.grid(row=row_idx, column=1, columnspan=2, padx=10, pady=default_pady, sticky="ew")
        row_idx += 1
        
        # Add Clip Button (after link and time entries)
        add_button = customtkinter.CTkButton(left_frame, text="Add Clip", corner_radius=widget_corner_radius, height=30) 
        add_button.grid(row=row_idx, column=0, columnspan=3, padx=10, pady=(10,default_pady[1]), sticky="ew")
        row_idx += 1

        # Quality (below link paste)
        customtkinter.CTkLabel(left_frame, text="Quality (for all clips):", font=label_font).grid(row=row_idx, column=0, padx=10, pady=default_pady, sticky="w")
        qualities = ["Best", "1080p", "720p", "480p"]
        quality_menu = customtkinter.CTkOptionMenu(left_frame, values=qualities, corner_radius=widget_corner_radius)
        quality_menu.grid(row=row_idx, column=1, columnspan=2, padx=10, pady=default_pady, sticky="ew")
        row_idx += 1
        
        # Download Destination
        customtkinter.CTkLabel(left_frame, text="Destination:", font=label_font).grid(row=row_idx, column=0, padx=10, pady=default_pady, sticky="w")
        dest_entry = customtkinter.CTkEntry(left_frame, width=200, corner_radius=widget_corner_radius)
        dest_entry.grid(row=row_idx, column=1, padx=10, pady=default_pady, sticky="ew")
        dest_browse_btn = customtkinter.CTkButton(left_frame, text="Browse", width=60, corner_radius=widget_corner_radius, command=lambda: self._browse_folder(dest_entry))
        dest_browse_btn.grid(row=row_idx, column=2, padx=(5,10), pady=default_pady)
        row_idx += 1

        # Cookies File
        customtkinter.CTkLabel(left_frame, text="Cookies File:", font=label_font).grid(row=row_idx, column=0, padx=10, pady=default_pady, sticky="w")
        cookies_entry = customtkinter.CTkEntry(left_frame, width=200, corner_radius=widget_corner_radius)
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
        download_btn = customtkinter.CTkButton(left_frame, text="Download All Clips", corner_radius=widget_corner_radius, height=35)
        download_btn.grid(row=row_idx, column=0, columnspan=3, padx=10, pady=button_pady, sticky="ew")

        # Right frame for thumbnails (placeholder)
        right_frame = customtkinter.CTkScrollableFrame(main_frame, label_text="Added Clips", label_font=("Roboto", 14, "bold"), corner_radius=8)
        right_frame.grid(row=0, column=1, sticky="nsew", padx=(5,10), pady=10)
        placeholder_label = customtkinter.CTkLabel(right_frame, text="Added clips with start/end times will appear here.", font=("Roboto", 12), text_color="gray60")
        placeholder_label.pack(padx=20, pady=20, expand=True)
        
        elements = {
            "link_entry": link_entry,
            "start_time_entry": start_time_entry,
            "end_time_entry": end_time_entry,
            "add_button": add_button,
            "quality_menu": quality_menu,
            "dest_entry": dest_entry,
            "cookies_entry": cookies_entry,
            "args_entry": args_entry,
            "download_btn": download_btn,
            "thumbnail_area": right_frame
        }
          # Connect buttons to functionality
        elements["add_button"].configure(command=lambda: self.app.downloader.add_clip_to_list(elements))
        elements["download_btn"].configure(command=lambda: self.app.downloader.download_multi_clip(elements))
        
        return elements
    
    def add_clip_to_list(self, elements):
        """Add a clip to the download list."""
        self.app.downloader.add_clip_to_list(elements)
