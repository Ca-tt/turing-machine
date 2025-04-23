from dataclasses import dataclass, field
from typing import Callable
from customtkinter import CTk, CTkToplevel, CTkLabel, CTkButton, CTkFrame, CTkFont

from components.widgets import widgets
from config.modals.modalConfigs import ALPHABET_MODAL_CONFIG


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
        alphabet_symbols.add("_")

        # alphabet_length: int = len(alphabet_symbols)

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

    

    def update_tape_symbol(self, event=None, selected_symbol: str = ""):
        self.update_cell_callback(self.index, selected_symbol)

        self.destroy()
