#!/usr/bin/env python3
"""
Test script to verify the progress bar functionality
"""
import tkinter as tk
import customtkinter
from src.utils.downloader import Downloader

def test_progress():
    """Test the progress bar with a simple download"""
    
    # Create a test window
    app = customtkinter.CTk()
    app.title("Progress Test")
    app.geometry("500x300")
    
    # Create progress frame
    progress_frame = customtkinter.CTkFrame(app)
    progress_frame.pack(pady=20, padx=20, fill="both", expand=True)
    
    # Progress bar
    progress_bar = customtkinter.CTkProgressBar(progress_frame, width=400)
    progress_bar.pack(pady=10)
    progress_bar.set(0)
    
    # Status label
    status_label = customtkinter.CTkLabel(progress_frame, text="Ready to download")
    status_label.pack(pady=5)
    
    # Store references in progress_frame
    progress_frame.progress_bar = progress_bar
    progress_frame.status_label = status_label
    
    # Test URL (short video)
    test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Rick Roll - should be quick
    
    def start_download():
        """Start a test download"""
        status_label.configure(text="Starting download...")
        
        # Create downloader
        downloader = Downloader()
        
        # Start download in background thread
        import threading
        def download_thread():
            try:
                success, message = downloader.download_video(
                    test_url,
                    "720p",
                    "c:/temp",  # Download to temp folder
                    None,  # No cookies
                    None,  # No custom args
                    progress_frame,  # Progress frame for updates
                    app  # App instance for UI updates
                )
                
                def final_update():
                    if success:
                        status_label.configure(text=f"Download completed: {message}")
                    else:
                        status_label.configure(text=f"Download failed: {message}")
                
                app.after(0, final_update)
                
            except Exception as e:
                def error_update():
                    status_label.configure(text=f"Error: {str(e)}")
                app.after(0, error_update)
        
        thread = threading.Thread(target=download_thread, daemon=True)
        thread.start()
    
    # Download button
    download_btn = customtkinter.CTkButton(
        progress_frame, 
        text="Test Download", 
        command=start_download
    )
    download_btn.pack(pady=10)
    
    # Instructions
    instructions = customtkinter.CTkLabel(
        progress_frame, 
        text="Click 'Test Download' to test the progress bar\nProgress should update in real-time during download",
        justify="center"
    )
    instructions.pack(pady=10)
    
    app.mainloop()

if __name__ == "__main__":
    test_progress()
