from dataclasses import dataclass, field
from typing import Callable
from customtkinter import CTk, CTkToplevel, CTkLabel, CTkButton, CTkFrame, CTkFont

# from components.frames.xy_frame import XYFrame,
from components.widgets import widgets


@dataclass
class ModalConfig:
    title: str = "Обрати знак з алфавiту"
    size: str = "300x150"


ALPHABET_MODAL_CONFIG = ModalConfig()


class Modal(CTkToplevel):
    def __init__(self, app: CTk, modal_title: str = "Modal", size: str = "400x300"):
        super().__init__(app)
        self.app = app
        self.title(modal_title)
        self.geometry(size)

        self.grab_set()


class AlphabetModal(Modal):
    def __init__(self, index: int, update_cell_callback: Callable, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.index = index
        self.update_cell_callback = update_cell_callback

    def place_widgets(self):
        widgets.alphabetmodal.frame = CTkFrame(self, height=50)
        widgets.alphabetmodal.frame.grid(row=0, column=0, padx=5, sticky="ew")

        self.columnconfigure(0, weight=1)

        alphabet_symbols = set(widgets.tape.alphabet_input.get())
        alphabet_symbols.add("_")

        for col, symbol in enumerate(alphabet_symbols):
            symbol_label = CTkLabel(
                master=widgets.alphabetmodal.frame,
                text=symbol,
                height=40,
                width=40,
                font=CTkFont(family="Arial", size=18),
                corner_radius=2,
                fg_color="white",
            )
            symbol_label.grid(row=0, column=col, padx=2, pady=5)

            symbol_label.bind("<Button-1>", lambda e, selected_symbol=symbol: self.update_tape_symbol(e, selected_symbol))

    def update_tape_symbol(self, event=None, selected_symbol: str = ""):
        self.update_cell_callback(self.index, selected_symbol)

        self.destroy()
