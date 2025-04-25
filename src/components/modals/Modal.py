from customtkinter import CTk, CTkToplevel, CTkLabel, CTkButton, CTkFrame, CTkFont

class Modal(CTkToplevel):
    def __init__(self, app: CTk, modal_title: str = "Modal", size: str = "400x300"):
        super().__init__(app)
        self.app = app
        self.title(modal_title)
        self.geometry(size)

        self.grab_set()


    def center_window(self, width: int, height: int, horizontal_offset: int = 0, vertical_offset: int = 0):
        """ centers the window """
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        
        self.geometry(f"{width}x{height}+{x+horizontal_offset}+{y+vertical_offset}")

