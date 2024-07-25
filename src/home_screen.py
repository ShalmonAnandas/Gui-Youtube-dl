import customtkinter
from downloader import Downloader

customtkinter.set_appearance_mode("system")


class MyCheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master, values):
        super().__init__(master)
        self.values = values
        self.checkboxes = []

        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        downloader = Downloader(self)

        self.title("CTkButton")
        self.geometry("1280x720")
        tabview = customtkinter.CTkTabview(master=self)
        tabview.pack(padx=20, pady=20, expand=True)
        tabview.add("tab 1")  # add tab at the end
        tabview.add("tab 2")  # add tab at the end
        tabview.set("tab 2")  # set currently visible tab

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame_1 = MyCheckboxFrame(
            tabview.tab("tab 1"), values=["value 1", "value 2", "value 3"]
        )
        self.checkbox_frame_1.grid(
            row=0, column=0, padx=10, pady=(10, 0), sticky="nsew"
        )
        self.checkbox_frame_2 = MyCheckboxFrame(
            tabview.tab("tab 1"), values=["option 1", "option 2"]
        )
        self.checkbox_frame_2.grid(
            row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="nsew"
        )

        self.button = customtkinter.CTkButton(
            tabview.tab("tab 1"), text="my button", command=self.button_callback
        )
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

    def button_callback(self):
        print("checked checkboxes:", self.checkbox_frame.get())


app = App()
app.mainloop()
