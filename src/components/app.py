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
from components.modals.AboutModal import AboutAppModal
from components.modals.TextModals import TextModal
from config.config import *
from config.texts.texts import TEXTS
from config.colors.colorsConfig import COLORS


#? UI
from components.widgets import widgets

from config.modals.modalConfigs import ALPHABET_MODAL_CONFIG, ABOUT_APP_MODAL, STOP_MODAL_CONFIG, FINIS_HMODAL_CONFIG
from components.modals.AlphabetModal import AlphabetModal



class App:
    def __init__(self):
        self._app = CTk()

        self.alphabet_modal = None
        self.about_app_modal = None
        self.stop_modal = None
        self.finish_modal = None


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


    def open_app(self):
        self._app.mainloop()


    def place_widgets(self):
        # ? [navbar]
        widgets.navbar.frame = CTkFrame(self._app, fg_color=COLORS.navbar.background)
        widgets.navbar.frame.grid(
            row=ROWS.navbar, column=0, columnspan=6, sticky="ew"
        )


        # ? about app button
        widgets.navbar.buttons.about_app = CTkButton(
            widgets.navbar.frame,
            text=TEXTS.navbar.about_app,
            fg_color=COLORS.navbar.buttons,
            height=NAVBAR.buttons_height,
            width=NAVBAR.buttons_width,
            command=self.open_about_modal,
        ).grid(
            row=ROWS.navbar,
            column=3,
            padx=NAVBAR.button_padx,
            pady=0,
        )

        # ? quit
        widgets.navbar.buttons.close_app = CTkButton(
            widgets.navbar.frame,
            text=TEXTS.navbar.close_app,
            fg_color=COLORS.navbar.buttons,
            height=NAVBAR.buttons_height,
            width=NAVBAR.buttons_width,
            command=self._app.destroy,
        ).grid(
            row=ROWS.navbar,
            column=4,
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


    def clear_textareas(self):
        """ clears textareas """
        widgets.task_description.input.delete("0.0", "end")
        widgets.comments.input.delete("0.0", "end")
    

    def open_alphabet_modal(self, event=None, index: int = 0, update_cell_callback: Optional[Callable] = None):
        if self.alphabet_modal is None or not self.alphabet_modal.winfo_exists():
            self.alphabet_modal = AlphabetModal(app=self._app, modal_title=ALPHABET_MODAL_CONFIG.title, size=ALPHABET_MODAL_CONFIG.size, index=index, update_cell_callback=update_cell_callback) 
            self.alphabet_modal.place_widgets()
        else:
            self.alphabet_modal.focus()
    

    def open_about_modal(self, event=None):
        if self.about_app_modal is None or not self.about_app_modal.winfo_exists():
            self.about_app_modal = AboutAppModal(app=self._app, modal_title=ABOUT_APP_MODAL.title, size=ABOUT_APP_MODAL.size)
            self.about_app_modal.place_widgets()
        else:
            self.about_app_modal.focus()
    
    
    def open_stop_modal(self, event=None):
        if self.stop_modal is None or not self.stop_modal.winfo_exists():
            self.stop_modal = TextModal(app=self._app, modal_title=STOP_MODAL_CONFIG.title, size=STOP_MODAL_CONFIG.size, width=STOP_MODAL_CONFIG.width, height=STOP_MODAL_CONFIG.height, text=TEXTS.modals.stop_modal_description)
            self.stop_modal.place_widgets(widgets.stop_modal.label)
        else:
            self.stop_modal.focus()
    
    def open_finish_modal(self, event=None):
        if self.finish_modal is None or not self.finish_modal.winfo_exists():
            self.finish_modal = TextModal(app=self._app, modal_title=FINIS_HMODAL_CONFIG.title, size=FINIS_HMODAL_CONFIG.size, width=FINIS_HMODAL_CONFIG.width, height=FINIS_HMODAL_CONFIG.height, text=TEXTS.modals.finish_modal_description)
            self.finish_modal.place_widgets(widgets.finish_modal.label)
        else:
            self.finish_modal.focus()

 
    


app = App()
