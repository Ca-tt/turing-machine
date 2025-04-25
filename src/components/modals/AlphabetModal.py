from dataclasses import dataclass, field
from typing import Callable
from customtkinter import CTk, CTkToplevel, CTkLabel, CTkButton, CTkFrame, CTkFont

#? components
from components.widgets import widgets
from components.modals.Modal import Modal

#? configs
from config.modals.modalConfigs import ALPHABET_MODAL_CONFIG


class AlphabetModal(Modal):
    def __init__(self, index: int, update_cell_callback: Callable, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #? center + shift down a little
        self.center_window(ALPHABET_MODAL_CONFIG.width, ALPHABET_MODAL_CONFIG.height, ALPHABET_MODAL_CONFIG.left_offset, ALPHABET_MODAL_CONFIG.top_offset)

        self.index = index
        self.update_cell_callback = update_cell_callback


    def place_widgets(self):
        widgets.alphabetmodal.frame = CTkFrame(self, height=50)
        widgets.alphabetmodal.frame.grid(row=0, column=0, padx=5, sticky="ew")

        self.columnconfigure(0, weight=1)

        alphabet_symbols = set(widgets.tape.alphabet_input.get())

        alphabet_symbols = self.sort_symbols(alphabet_symbols)
        alphabet_symbols.append("_")

        for column_index, symbol in enumerate(alphabet_symbols):
            first_row = 0
            next_row: int = column_index // ALPHABET_MODAL_CONFIG.cells_in_row

            #? start a column with a new row
            if next_row != first_row:
                column_index = column_index % ALPHABET_MODAL_CONFIG.cells_in_row

            symbol_label = CTkLabel(
                master=widgets.alphabetmodal.frame,
                text=symbol,
                height=40,
                width=40,
                font=CTkFont(family="Arial", size=18),
                corner_radius=2,
                fg_color="white",
            )
            symbol_label.grid(row=next_row, column=column_index, padx=2, pady=5)
            symbol_label.bind("<Button-1>", lambda e, selected_symbol=symbol: self.update_tape_symbol(e, selected_symbol))


    @staticmethod
    def sort_symbols(symbols_set: set):
        return sorted(symbols_set)


    def update_tape_symbol(self, event=None, selected_symbol: str = ""):
        self.update_cell_callback(self.index, selected_symbol)

        self.destroy()

