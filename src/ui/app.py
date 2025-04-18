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
        set_appearance_mode(mode_string=UI.theme)
        set_default_color_theme(color_string=UI.colors)

        self._app.title(string=UI.title)
        self._app.geometry(geometry_string=UI.app_size)

        self._app.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

    def open(self):
        self._app.mainloop()

    def place_widgets(self):
        # ? [navbar]
        widgets.navbar.frame = CTkFrame(self._app, fg_color=COLORS.navbar.background)
        widgets.navbar.frame.grid(
            row=UI.rows.navbar, column=0, columnspan=6, sticky="ew"
        )

        # ? quit
        widgets.navbar.buttons.close_app = CTkButton(
            widgets.navbar.frame,
            text="Закрити",
            fg_color=COLORS.navbar.buttons,
            height=UI.navbar.buttons.height,
            width=UI.navbar.buttons.width,
            command=self._app.destroy,
        ).grid(
            row=UI.rows.navbar,
            column=2,
            padx=UI.navbar.buttons.padx,
            pady=0,
        )

        widgets.description.label = CTkLabel(
            self._app, text=f"{TEXT.tape.state_label}: {TAPE.state}"
        )
        widgets.description.label.grid(
            row=UI.rows.state_label, column=0, columnspan=5, pady=5
        )

        # ? state label
        widgets.tape.state_label = CTkLabel(
            self._app, text=f"{TEXT.tape.state_label}: {TAPE.state}"
        )
        widgets.tape.state_label.grid(
            row=UI.rows.state_label, column=0, columnspan=5, pady=5
        )


app = App()
