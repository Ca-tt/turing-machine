from customtkinter import (
    CTk,
    CTkButton,
    CTkFrame,
    CTkLabel,
    set_appearance_mode,
    set_default_color_theme,
)

# ? configs
from ui.config import UI, TAPE, TEXT, COLORS

# ? UI
from ui.widgets import widgets


class App:
    def __init__(self):
        self._app = CTk()

    def set_ui_settings(self):
        set_appearance_mode(UI["theme"])
        set_default_color_theme(UI["colors"])

        self._app.title(UI["title"])
        self._app.geometry(UI["size"])

        self._app.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

    def open(self):
        self._app.mainloop()


    def place_widgets(self):
        # ? [navbar]
        widgets["navbar"]["frame"] = CTkFrame(self._app, fg_color=COLORS["navbar"]["background"])
        widgets["navbar"]["frame"].grid(row=UI["rows"]["navbar"], column=0, columnspan=6, sticky="ew")

        # ? quit
        widgets["navbar"]["buttons"]["close_app"] =CTkButton(
            widgets["navbar"]["frame"],
            text="Закрити",
            fg_color=COLORS["navbar"]["buttons"],
            height=UI["navbar"]["buttons"]["height"],
            width=UI["navbar"]["buttons"]["width"],
            command=self._app.destroy,
        ).grid(
            row=UI["rows"]["navbar"],
            column=2,
            padx=UI["navbar"]["buttons"]["padx"],
            pady=0,
        )

        widgets["tape"]["state"] = CTkLabel(self._app, text=f"State: {TAPE['state']}")
        widgets["tape"]["state"].grid(
            row=UI["rows"]["state_label"], column=0, columnspan=5, pady=5
        )


app = App()