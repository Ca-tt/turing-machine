from typing import Callable, Optional
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

#? configs
from config.config import *
from config.texts.texts import TEXTS
from config.colors.colorsConfig import COLORS


#? UI
from components.widgets import widgets

from config.modals.modalConfigs import ALPHABET_MODAL_CONFIG
from components.modal import AlphabetModal



class App:
    def __init__(self):
        self._app = CTk()

        self.alphabet_modal = None


    def set_ui_settings(self):
        set_appearance_mode(mode_string=APP_WINDOW.theme)
        set_default_color_theme(color_string=APP_WINDOW.colors)

        self._app.title(string=APP_WINDOW.title)
        self._app.geometry(geometry_string=APP_WINDOW.window_size)

        self._app.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.center_window(APP_WINDOW.width, APP_WINDOW.height, 0, 0)


    def center_window(self, width: int, height: int, horizontal_offset: int = 0, vertical_offset: int = 0):
        """ centers the window """
        screen_width = self._app.winfo_screenwidth()
        screen_height = self._app.winfo_screenheight()
        
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        
        self._app.geometry(f"{width}x{height}+{x+horizontal_offset}+{y+vertical_offset}")


    def open(self):
        self._app.mainloop()


    def place_widgets(self):
        # ? [navbar]
        widgets.navbar.frame = CTkFrame(self._app, fg_color=COLORS.navbar.background)
        widgets.navbar.frame.grid(
            row=ROWS.navbar, column=0, columnspan=6, sticky="ew"
        )

        # ? quit
        widgets.navbar.buttons.close_app = CTkButton(
            widgets.navbar.frame,
            text=TEXTS.navbar.close_app_button,
            fg_color=COLORS.navbar.buttons,
            height=NAVBAR.button_height,
            width=NAVBAR.button_width,
            command=self._app.destroy,
        ).grid(
            row=ROWS.navbar,
            column=2,
            padx=NAVBAR.button_padx,
            pady=0,
        )

        #? task description
        widgets.task_description.label = CTkLabel(
            self._app, text=f"{TEXTS.task_description.label}", anchor="w"
        )
        widgets.task_description.label.grid(
            row=ROWS.task_description_label, column=0, columnspan=5, padx=TASK_DESCRIPTION.padx, pady=(5), sticky="w"
        )
        widgets.task_description.input = CTkTextbox(
            self._app,
            height=TASK_DESCRIPTION.input_height
        )
        widgets.task_description.input.grid(
            row=ROWS.task_description_input, column=0, columnspan=5, padx=TASK_DESCRIPTION.padx, pady=(0), sticky="we", 
        )

        #? comment labels
        widgets.comments.label = CTkLabel(
            self._app, text=f"{TEXTS.comments.label}", anchor="e"
        )
        widgets.comments.label.grid(
            row=ROWS.rules_comments_labels, column=3, columnspan=3, padx=COMMENTS.padx, pady=(5)
        )

        widgets.comments.input = CTkTextbox(
            self._app,
            height=COMMENTS.input_height
        )
        widgets.comments.input.grid(
            row=ROWS.rules_inputs, column=3, columnspan=2, padx=COMMENTS.padx, pady=(0), sticky="nwes" 
        )


        # ? state label
        widgets.tape.state_label = CTkLabel(
            self._app, text=f"{TEXTS.tape.state_label}: {TAPE.state}", anchor="center"
        )
        widgets.tape.state_label.grid(
            row=ROWS.state_label, column=0, columnspan=2, padx=40, pady=5, sticky="we"
        )
    
    def open_alphabet_modal(self, event=None, index: int = 0, update_cell_callback: Optional[Callable] = None):
        if self.alphabet_modal is None or not self.alphabet_modal.winfo_exists():
            self.alphabet_modal = AlphabetModal(app=self._app, modal_title=ALPHABET_MODAL_CONFIG.title, size=ALPHABET_MODAL_CONFIG.size, index=index, update_cell_callback=update_cell_callback) 
            self.alphabet_modal.place_widgets()
        else:
            self.alphabet_modal.focus()

    


app = App()
