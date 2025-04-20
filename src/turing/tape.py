from customtkinter import (
    CTkButton,
    CTkEntry,
    CTkLabel,
    CTkFrame
)

# ? UI
from ui.widgets import widgets
from ui.xy_frame import XYFrame

# ? configs
from ui.config import UI, TAPE, TEXTS, COLORS

#? parts
from ui.app import App, app
from turing.rules import Rules


class Tape:
    __tape_instance = None

    cells: list[CTkLabel]
    symbols: list[str]
    is_running: bool

    head_position: int
    state: str = "q0"

    def __new__(cls, *args, **kwargs):
        if cls.__tape_instance is None:
            cls.__tape_instance = super().__new__(cls)
            cls.__tape_instance.symbols = [TAPE.sign] * TAPE.cells
            cls.__tape_instance.cells = []
            cls.__tape_instance.head_position = TAPE.position
            cls.__tape_instance.state = "q0"
            cls.__tape_instance.is_running = False

        return cls.__tape_instance


    def __init__(self):
        self.app = app._app

        #? parts
        self.Rules = Rules()


    def create_widgets(self):
        #? cells
        widgets.tape.cells_frame = XYFrame(
            self.app,
            height=UI.tape.height,
            scrollbar_width=UI.tape.scrollbar.height,
        )
        widgets.tape.cells_frame.grid(
            row=UI.rows.tape,
            column=UI.tape.column.start,
            columnspan=UI.tape.column.end,
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

        widgets.tape.alphabet_input = CTkEntry(self.app, width=200)
        widgets.tape.alphabet_input.grid(
            row=UI.rows.alphabet, column=1, columnspan=3, pady=20, padx=0, sticky="we"
        )
        widgets.tape.alphabet_input.insert(0, TAPE.input)

        self.create_cells()

        # ? [set tape] signs button
        widgets.tape.buttons.set_tape_button = CTkButton(
            self.app, text=TEXTS.button.set_tape_button, command=self.set_symbols
        ).grid(row=UI.rows.alphabet, column=4, padx=5, pady=5)


        widgets.tape.buttons_frame = CTkFrame(self.app, fg_color="transparent")
        widgets.tape.buttons_frame.grid(row=UI.rows.tape_buttons, column=0, columnspan=5)


        # ? step [left] / [right] buttons
        widgets.tape.buttons.move_left_button = CTkButton(
            widgets.tape.buttons_frame, text=TEXTS.button.step_left_button, command=self.move_left
        ).grid(row=UI.rows.tape_buttons, column=0, padx=5, pady=10)

        widgets.tape.buttons.move_right_button = CTkButton(
            widgets.tape.buttons_frame, text=TEXTS.button.step_right_button, command=self.move_right
        ).grid(row=UI.rows.tape_buttons, column=1, padx=5, pady=5)

        # ? [step], [run], [stop] butons
        widgets.tape.buttons.step_button = CTkButton(
            widgets.tape.buttons_frame, text=TEXTS.button.step_button, command=self.make_step
        ).grid(row=UI.rows.tape_buttons, column=2, padx=5, pady=5)

        widgets.tape.buttons.run_button = CTkButton(
            widgets.tape.buttons_frame, text=TEXTS.button.run_button, command=self.run
        ).grid(row=UI.rows.tape_buttons, column=3, padx=5, pady=5)

        widgets.tape.buttons.stop_button = CTkButton(
            widgets.tape.buttons_frame, text=TEXTS.button.stop_button, command=self.stop
        ).grid(row=UI.rows.tape_buttons, column=4, padx=5, pady=5)


    def create_cells(self):
        self.cells = []
        cells_len = len(self.symbols)

        # print("🐍 self.symbols",self.symbols)
        # print("🐍 cells_len (create_cells)",cells_len)
        
        # ? create tape cells
        for i in range(cells_len):
            label = CTkLabel(
                widgets.tape.cells_frame,
                text=TAPE.sign,
                width=20,
                font=("Courier", 14),
                fg_color=("white", COLORS.tape.cell),
                corner_radius=5,
            )
            label.grid(row=UI.rows.tape, column=i, padx=2)
            self.cells.append(label)

        # print("🐍  self.cells len (after create_cells): ",len(self.cells))

    



    def add_cell(self, new_cell_position):
        new_cell_sign = "_"
        # print("🐍 self.symbols (before add_cell): ",self.symbols)

        label = CTkLabel(
            widgets.tape.cells_frame,
            text=new_cell_sign,
            width=20,
            font=("Courier", 14),
            fg_color=("white", COLORS.tape.cell),
            corner_radius=5,
        )

        # print("🐍 new_cell_position",new_cell_position)
        if new_cell_position < 0:
            new_cell_position = 0
            #? shift head left
            self.head_position += 1
            # print("shift left")
        else:
            new_cell_position = len(self.cells)
            #? shift head right
            self.head_position -= 1
            # print("shift right")

        # print(f"inserting cell to position {new_cell_position}")
        # print(f"head position after inserting: {self.head_position}")

        self.symbols.insert(new_cell_position, new_cell_sign)
        self.cells.insert(new_cell_position, label)

        # print("🐍 self.symbols (after add_cell): ",self.symbols)
        # print("🐍 self.cells len (after add_cell): ", len(self.cells))

        # print(f"{'='*10}")

        label.grid(row=UI.rows.tape, column=new_cell_position, padx=2)

        self.create_cells()
        self.set_symbols()


    def set_symbols(self):
        #? clear previous input
        self.clear_cells()
        # print("set_symbols working")

        symbols = list(widgets.tape.alphabet_input.get())

        tape_len = len(self.cells)
        symbols_len = len(symbols) 
        # print("🐍 tape_len",tape_len)

        # print("🐍 current head_position: ",self.current_position)
    
        #? shift_from_center calculations examples 
        # (3 // 2 = 1 index, 5 // 2 = 2 index of 4 elements)
        # 3, 5, 11 - place leftside or rightside (your choose 0 or 1)
        # (3 // 2 = 1 index, 5 // 2 = 2 index of 4 elements)

        #? set 0 to shift odd symbols leftside
        #? set 1 to shift rightside
        odd_shift = 1 
        shift_from_center = symbols_len // 2 

        #? find the center index of odd or even symbols count 
        if symbols_len % 2 == 0:
            shift_from_center -= odd_shift 

        # print("🐍 self.head_position",self.head_position)

        for index, symbol in enumerate(symbols):
            new_position = -(index - shift_from_center) # -3, -2, -1, 0, 1, 2, 3
            cell_position = self.head_position - new_position
            # print("🐍 new cell_position",cell_position)

            #? check for the need of tape extension
            #? extend the boundaries when needed
            if cell_position < 0 or cell_position > tape_len - 1:
                self.add_cell(cell_position)
                return


            self.symbols[cell_position] = symbol
        # print("🐍 self.symbols (after set_cells_text)",self.symbols)
        # print(f"{'='*10}")

        self.update_cell_texts()


    # ? update cells color and symbol
    def update_cell_texts(self):
        # print("update_cell_texts working...")
        # print("🐍 self.symbols: ",self.symbols)
        # print("🐍 self.cells len: ", len(self.cells))
        # print("🐍 self.head_position",self.head_position)
        # print(f"{'='*10}")

        for i, symbol in enumerate(self.symbols):
            if i == self.head_position:
                self.cells[i].configure(fg_color=COLORS.tape.highlight)
            else:
                self.cells[i].configure(fg_color=("white", COLORS.tape.cell))
            self.cells[i].configure(text=symbol)

        widgets.tape.state_label.configure(text=f"{TEXTS.tape.state_label}: {self.state}")


    def clear_cells(self):
        for i, cell in enumerate(self.cells):
            self.symbols[i] = "_"
            cell.configure(text="_")
        
        # self.cells = []


    def extend_tape(self):
        #? here will goes all check / ifs
        pass

    def extend_side(self, side="right"):
        #! Когда нужно, добавляем ячеек в левую или правую сторону
        #! Вычисляем это, когда (число знаков из input // 2) > max_tape_cells (21) - tape_position (19)
        #! или когда (число знаков из input // 2) > tape_position (3) - min_tape_cells (0)
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
            and (self.state, self.symbols[self.head_position]) in self.Rules.rules
        ):
            self.make_step()
            self.app.after(500, self.run_until_stop)
        else:
            self.is_running = False

    def make_step(self):
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
