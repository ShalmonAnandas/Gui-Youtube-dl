import customtkinter
from src.utils.download_manager import DownloadManager
from src.common_widgets.checkbox_builder import MyCheckboxFrame

customtkinter.set_appearance_mode("system")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Download Manager")
        self.geometry("1280x720")
        self.downloader = DownloadManager(self)
        
        self.tabview = customtkinter.CTkTabview(master=self)
        self.tabview.pack(padx=20, pady=20, expand=True, fill="both")
        self.tabview.add("tab 1")
        self.tabview.add("tab 2")

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.button = customtkinter.CTkButton(
            self.tabview.tab("tab 1"),
            text="Download",
            command=self.button_callback
        )
        self.button.grid(
            row=0, column=0, padx=10, pady=10, sticky="nsew", columnspan=2
        )

    def button_callback(self):
        self.downloader.button_function()

app = App()
app.mainloop()