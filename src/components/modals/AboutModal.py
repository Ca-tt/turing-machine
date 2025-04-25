from dataclasses import dataclass, field
from typing import Callable
from customtkinter import CTk, CTkToplevel, CTkLabel, CTkButton, CTkFrame, CTkFont, CTkTextbox

#? components
from components.widgets import widgets
from components.modals.Modal import Modal

#? configs
from config.modals.modalConfigs import ABOUT_APP_MODAL
from config.texts.texts import TEXTS

class AboutAppModal(Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.center_window(width=ABOUT_APP_MODAL.width, height=ABOUT_APP_MODAL.height) 



    def place_widgets(self):
        widgets.aboutmodal.textbox = CTkTextbox(self, font=(CTkFont(family="Arial", size=14)))
        widgets.aboutmodal.textbox.grid(row=0, column=0, sticky="nwse")
        widgets.aboutmodal.textbox.insert(0.0, TEXTS.about.app_description)