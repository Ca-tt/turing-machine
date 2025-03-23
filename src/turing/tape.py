from customtkinter import (
    CTk,
    CTkButton,
    CTkEntry,
    CTkFrame,
    CTkLabel,
)

# ? UI
from ui.widgets import widgets
from ui.xy_frame import XYFrame

# ? configs
from ui.config import UI, TAPE, TEXT, COLORS


class Tape:
    def __init__(self, app):
        self.app = app

        self.tape_symbols: list[str] = [TAPE["sign"]] * TAPE["cells"]
        self.head_position: int = TAPE["position"]
        self.is_running = False

        self.state: str = "q0"

        # ? widgets
        self.cells: list[CTkLabel] = []  # tape labels


    def create_widgets(self):
        self.tape_frame = XYFrame(
            self.app,
            height=UI["tape"]["height"],
            scrollbar_width=UI["tape"]["scrollbar"]["height"],
        )
        self.tape_frame.grid(
            row=UI["rows"]["tape"],
            column=UI["tape"]["column"]["start"],
            columnspan=UI["tape"]["column"]["end"],
            padx=2,
            sticky="ew",
        )

        # ? [input] field for numbers or characters
        self.input_entry = CTkEntry(self.app, width=200)
        self.input_entry.grid(row=UI["rows"]["input"], column=0, columnspan=3, pady=20)
        self.input_entry.insert(0, TAPE["input"])

        self.create_cells()

        # ? [set tape] signs button
        widgets["tape"]["buttons"]["set_tape_text"] = CTkButton(
            self.app, text=TEXT["button"]["set_tape"], command=self.set_cells_text
        ).grid(row=UI["rows"]["input"], column=3, padx=5, pady=5)

        # ? step [left] / [right] buttons
        widgets["tape"]["buttons"]["move_left"] =CTkButton(
            self.app, text=TEXT["button"]["step_left"], command=self.move_left
        ).grid(row=UI["rows"]["buttons"], column=0, pady=5)

        widgets["tape"]["buttons"]["move_right"] = CTkButton(
            self.app, text=TEXT["button"]["step_right"], command=self.move_right
        ).grid(row=UI["rows"]["buttons"], column=1, pady=5)

        # ? [step], [run], [stop] butons
        widgets["tape"]["buttons"]["step"] = CTkButton(self.app, text=TEXT["button"]["step"], command=self.make_step).grid(
            row=UI["rows"]["buttons"], column=2, pady=5
        )

        widgets["tape"]["buttons"]["run"] = CTkButton(self.app, text=TEXT["button"]["run"], command=self.run).grid(
            row=UI["rows"]["buttons"], column=3, pady=5
        )

        widgets["tape"]["buttons"]["stop"] = CTkButton(self.app, text=TEXT["button"]["stop"], command=self.stop).grid(
            row=UI["rows"]["buttons"], column=4, pady=5
        )

    def create_cells(self):
        # ? create tape cells
        for i in range(TAPE["cells"]):
            label = CTkLabel(
                self.tape_frame,
                text=TAPE["sign"],
                width=20,
                font=("Courier", 14),
                fg_color=("white", COLORS["tape"]["cell"]),
                corner_radius=5,
            )
            label.grid(row=UI["rows"]["tape"], column=i, padx=2)
            self.cells.append(label)

    def set_cells_text(self):
        input_text = self.input_entry.get()
        for i, char in enumerate(input_text):
            if i < len(self.tape_symbols):
                self.tape_symbols[self.head_position - len(input_text) // 2 + i] = char
        self.update_cells()

    # ? update cells color and symbol
    def update_cells(self):
        # print("🐍 self.tape_symbols",self.tape_symbols)
        # print("🐍 self.cells",self.cells)

        for i, symbol in enumerate(self.tape_symbols):
            if i == self.head_position:
                self.cells[i].configure(fg_color=COLORS["tape"]["highlight"])
            else:
                self.cells[i].configure(fg_color=("white", COLORS["tape"]["cell"]))

            self.cells[i].configure(text=symbol)
        widgets["tape"]["state"].configure(text=f"State: {self.state}")

    def clear_tape(self):
        pass

    def run(self):
        self.is_running = True
        self.run_until_stop()

    def stop(self):
        self.is_running = False
        pass

    # ? make tape running infinitely
    def run_until_stop(self):
        if (
            self.is_running
            and (self.state, self.tape_symbols[self.head_position]) in self.rules
        ):
            self.make_step()
            self.app.after(500, self.run_until_stop)
        else:
            self.is_running = False

    def make_step(self):
        self.read_rules()

        current_symbol = self.tape_symbols[self.head_position]

        if (self.state, current_symbol) in self.rules:
            # ? get (next state, write symbol, direction) tuple
            next_state, write_symbol, move = self.rules[(self.state, current_symbol)]

            # ? set next symbol for the new cell
            self.tape_symbols[self.head_position] = write_symbol

            # ? update the state
            self.state = next_state

            # ? move cursor right or left
            if move == "L":
                self.move_left()
            elif move == "R":
                self.move_right()

            self.update_tape_display()

    def move_left(self):
        if self.head_position > 0:
            self.head_position -= 1
            self.update_tape_display()

    def move_right(self):
        if self.head_position < len(self.tape_symbols) - 1:
            self.head_position += 1
            self.update_tape_display()
