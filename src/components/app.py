from customtkinter import (
    CTk,
    CTkButton,
    CTkFrame,
    CTkLabel,
    CTkTextbox,
    CTkEntry,
    set_appearance_mode,
    set_default_color_theme,
)

# ? configs
from config.config import *

# ? UI
from components.widgets import widgets


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
            text=TEXTS.navbar.close_app_button,
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

        #? task description
        widgets.task_description.label = CTkLabel(
            self._app, text=f"{TEXTS.task_description.label}", anchor="w"
        )
        widgets.task_description.label.grid(
            row=UI.rows.task_description_label, column=0, columnspan=5, padx=TASK_DESCRIPTION.padx, pady=(5), sticky="w"
        )
        widgets.task_description.input = CTkTextbox(
            self._app,
            height=TASK_DESCRIPTION.input_height
        )
        widgets.task_description.input.grid(
            row=UI.rows.task_description_input, column=0, columnspan=5, padx=TASK_DESCRIPTION.padx, pady=(0), sticky="we", 
        )

        #? comment labels
        widgets.comments.label = CTkLabel(
            self._app, text=f"{TEXTS.comments.label}", anchor="e"
        )
        widgets.comments.label.grid(
            row=UI.rows.rules_comments_labels, column=3, columnspan=3, padx=COMMENTS.padx, pady=(5)
        )

        widgets.comments.input = CTkTextbox(
            self._app,
            height=COMMENTS.input_height
        )
        widgets.comments.input.grid(
            row=UI.rows.rules_inputs, column=3, columnspan=2, padx=COMMENTS.padx, pady=(0), sticky="nwes" 
        )


        # ? state label
        widgets.tape.state_label = CTkLabel(
            self._app, text=f"{TEXTS.tape.state_label}: {TAPE.state}", anchor="center"
        )
        widgets.tape.state_label.grid(
            row=UI.rows.state_label, column=0, columnspan=2, padx=40, pady=5, sticky="we"
        )


app = App()
