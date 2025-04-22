from customtkinter import (
    CTkButton,
    CTkEntry,
    CTkLabel,
    CTkFrame
)

# ? UI
from components.widgets import widgets
from components.frames.xy_frame import XYFrame

# ? configs
from config.config import ARROWS_CONFIG, UI, TAPE_CONFIG, TEXTS, COLORS

#? parts
from components.app import App, app
from components.turing.rules import Rules


class Tape:
    _instance = None

    cells: list[CTkLabel]
    symbols: list[str]
    is_running: bool

    head_position: int
    state: str = "q0"

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.symbols = [TAPE_CONFIG.cell_sign] * TAPE_CONFIG.cells
            cls._instance.cells = []
            cls._instance.head_position = TAPE_CONFIG.cells // 2
            cls._instance.state = "q0"
            cls._instance.is_running = False

        return cls._instance


    def __init__(self):
        self.app = app._app

        #? parts
        self.Rules = Rules()


    def create_widgets(self):
        #? cells frame
        widgets.tape.cells_frame = XYFrame(
            self.app,
            height=UI.tape_cells.height,
            scrollbar_width=UI.tape_cells.scrollbar.height,
        )
        widgets.tape.cells_frame.grid(
            row=UI.rows.cells,
            column=UI.tape_cells.column.start,
            columnspan=UI.tape_cells.column.end,
            padx=2,
            sticky="ew",
        )

        # ? alphabet label
        widgets.tape.alphabet_label = CTkLabel(
            self.app, text=f"{TEXTS.tape.alphabet_label}"
        )
        widgets.tape.alphabet_label.grid(
            row=UI.rows.alphabet, column=0, padx=5, pady=(5)
        )

        # ? alphabet input
        widgets.tape.alphabet_input = CTkEntry(self.app, width=200)
        widgets.tape.alphabet_input.grid(
            row=UI.rows.alphabet, column=1, columnspan=3, pady=20, padx=0, sticky="we"
        )
        widgets.tape.alphabet_input.insert(0, TAPE_CONFIG.alphabet)

        self.create_cells()

        # ? [set tape] signs button
        widgets.tape.buttons.set_tape_button = CTkButton(
            self.app, text=TEXTS.button.set_tape, command=self.set_symbols
        ).grid(row=UI.rows.alphabet, column=4, padx=5, pady=5)


        # ? step [left] / [right] buttons
        # ? [step], [run], [stop] butons
        widgets.tape.buttons_frame = CTkFrame(self.app, fg_color="transparent")
        widgets.tape.buttons_frame.grid(row=UI.rows.tape_buttons, column=0, columnspan=5)
        
        widgets.tape.buttons.move_left_button = CTkButton(
            widgets.tape.buttons_frame, text=TEXTS.button.step_left, command=self.move_left
        ).grid(row=UI.rows.tape_buttons, column=0, padx=5, pady=10)

        widgets.tape.buttons.move_right_button = CTkButton(
            widgets.tape.buttons_frame, text=TEXTS.button.step_right, command=self.move_right
        ).grid(row=UI.rows.tape_buttons, column=1, padx=5, pady=5)

        widgets.tape.buttons.step_button = CTkButton(
            widgets.tape.buttons_frame, text=TEXTS.button.step, command=self.make_step
        ).grid(row=UI.rows.tape_buttons, column=2, padx=5, pady=5)

        widgets.tape.buttons.run_button = CTkButton(
            widgets.tape.buttons_frame, text=TEXTS.button.run, command=self.run
        ).grid(row=UI.rows.tape_buttons, column=3, padx=5, pady=5)

        widgets.tape.buttons.stop_button = CTkButton(
            widgets.tape.buttons_frame, text=TEXTS.button.stop, command=self.stop
        ).grid(row=UI.rows.tape_buttons, column=4, padx=5, pady=5)

        #? arrows
        widgets.tape.left_arrow = CTkButton(
            self.app, text=TEXTS.button.left_arrow, width=ARROWS_CONFIG.width, height=ARROWS_CONFIG.height, fg_color=ARROWS_CONFIG.bg_color, command=lambda: widgets.tape.cells_frame.move_scrollbar(-ARROWS_CONFIG.move_size)
        )
        widgets.tape.right_arrow = CTkButton(
            self.app, text=TEXTS.button.right_arrow, width=ARROWS_CONFIG.width, height=ARROWS_CONFIG.height, fg_color=ARROWS_CONFIG.bg_color, command=lambda: widgets.tape.cells_frame.move_scrollbar(ARROWS_CONFIG.move_size)
        )

        widgets.tape.left_arrow.grid(row=UI.rows.arrows, column=0, padx=5, pady=5, sticky="w")
        widgets.tape.right_arrow.grid(row=UI.rows.arrows, column=4, padx=5, pady=5, sticky="e")



    def create_cells(self):
        self.cells = []
        cells_len = len(self.symbols)

        cells_center = cells_len // 2
        cells_number = 0

        #? cell order numbers
        for i in range(cells_len):
            
            #? negatives (-34, -33, -32)
            if i < cells_center:
                cells_number = -cells_center + i

            #? center (0)
            if i == cells_center:
                cells_number = 0

            #? positive numbers
            if i > cells_center:
                cells_number = i - cells_center 

            cell_number_label = CTkLabel(
                widgets.tape.cells_frame,
                text=str(cells_number),
                width=15,
                font=("Courier", 12),
                fg_color=("transparent"),
                corner_radius=5,
            )
            cell_number_label.grid(row=UI.rows.cell_numbers, column=i, padx=2)

        
        #? create tape cells
        for i in range(cells_len):
            #? cells
            cell_label = CTkLabel(
                widgets.tape.cells_frame,
                text=TAPE_CONFIG.cell_sign,
                width=20,
                font=("Courier", 14),
                fg_color=("white", COLORS.tape.cell),
                corner_radius=5,
            )
            cell_label.grid(row=UI.rows.cells, column=i, padx=2)
            cell_label.bind("<Button-1>", lambda event, index=i: app.open_alphabet_modal(event, index, update_cell_callback=self.update_cell))
            self.cells.append(cell_label)
            
            #? access cells globally
            widgets.tape.cells.append(cell_label)


    def add_cell(self, new_cell_position):
        new_cell_sign = "_"

        label = CTkLabel(
            widgets.tape.cells_frame,
            text=new_cell_sign,
            width=20,
            font=("Courier", 14),
            fg_color=("white", COLORS.tape.cell),
            corner_radius=5,
        )

        if new_cell_position < 0:
            new_cell_position = 0
            #? shift head left
            self.head_position += 1
        else:
            new_cell_position = len(self.cells)
            #? shift head right
            self.head_position -= 1

        self.symbols.insert(new_cell_position, new_cell_sign)
        self.cells.insert(new_cell_position, label)

        label.grid(row=UI.rows.cells, column=new_cell_position, padx=2)

        self.create_cells()
        self.set_symbols()


    def set_symbols(self):
        #? clear previous input
        self.clear_cells()
        symbols = list(widgets.tape.alphabet_input.get())

        tape_len = len(self.cells)
        symbols_len = len(symbols) 
    
        #? shift_from_center calculations examples 
        #? (3 // 2 = 1 index, 5 // 2 = 2 index of 4 elements)
        #? 3, 5, 11 - place leftside or rightside (your choose 0 or 1)
        #? (3 // 2 = 1 index, 5 // 2 = 2 index of 4 elements)

        #? set 0 to shift odd symbols leftside
        #? set 1 to shift rightside
        odd_shift = 1 
        symbols_center_position = symbols_len // 2 

        #? find the center index of odd or even symbols count 
        if symbols_len % 2 == 0:
            symbols_center_position -= odd_shift 

        for index, symbol in enumerate(symbols):
            new_position = -(index - symbols_center_position) # -3, -2, -1, 0, 1, 2, 3
            cell_position = self.head_position - new_position

            #? check for the need of tape extension
            #? extend the boundaries when needed
            if cell_position < 0 or cell_position > tape_len - 1:
                self.add_cell(cell_position)
                return

            self.symbols[cell_position] = symbol

        self.update_cell_texts()


    # ? update cells color and symbol
    def update_cell_texts(self):
        for i, symbol in enumerate(self.symbols):
            if i == self.head_position:
                self.cells[i].configure(fg_color=COLORS.tape.highlight)
            else:
                self.cells[i].configure(fg_color=("white", COLORS.tape.cell))
            self.cells[i].configure(text=symbol)

        widgets.tape.state_label.configure(text=f"{TEXTS.tape.state_label}: {self.state}")


    def update_cell(self, index: int, new_symbol: str):
        self.cells[index].configure(text=new_symbol)
        self.symbols[index] = new_symbol



    def clear_cells(self):
        for i, cell in enumerate(self.cells):
            self.symbols[i] = "_"
            cell.configure(text="_")



    def run(self):
        if self.state == "q0":
            self.state = "q1"
        self.is_running = True
        self.run_until_stop()

    def stop(self):
        self.is_running = False
        self.state = "q0"

    # ? make tape running infinitely
    def run_until_stop(self):
        if (
            self.is_running
            and (self.state, self.symbols[self.head_position]) in self.Rules.rules
        ):
            self.make_step()
            self.app.after(500, self.run_until_stop)
        else:
            self.stop()

    def make_step(self):
        if self.state == "q0":
            self.state = "q1"
    
        self.Rules.read_rules()

        current_symbol = self.symbols[self.head_position]

        if (self.state, current_symbol) in self.Rules.rules:
            # ? get (next state, write symbol, direction) tuple
            next_state, write_symbol, move = self.Rules.rules[(self.state, current_symbol)]

            # ? set next symbol for the new cell
            self.symbols[self.head_position] = write_symbol

            # ? update the state
            self.state = next_state

            # ? move cursor right or left
            if move == "L":
                self.move_left()
            elif move == "R":
                self.move_right()

            self.update_cell_texts()

    def move_left(self):
        if self.head_position > 0:
            self.head_position -= 1
            self.update_cell_texts()

    def move_right(self):
        if self.head_position < len(self.symbols) - 1:
            self.head_position += 1
            self.update_cell_texts()
