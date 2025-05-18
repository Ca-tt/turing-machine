from dataclasses import dataclass, field
from typing import Callable
from customtkinter import CTk, CTkToplevel, CTkLabel, CTkButton, CTkFrame, CTkFont, CTkTextbox

#? components
from components.widgets import widgets
from components.modals.Modal import Modal

#? configs
from config.modals.modalConfigs import ABOUT_APP_MODAL
from config.texts.texts import TEXTS

class TextModal(Modal):
    def __init__(self, text: str, width: int, height: int, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.text = text

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.center_window(width=width, height=height) 


    def place_widgets(self, widget):
        widget = CTkLabel(self, text=self.text, font=(CTkFont(family="Arial", size=14)))
        widget.grid(row=0, column=0, sticky="nwse")