from enum import Enum
from tkinter import END

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
from config.texts.texts import TEXTS
from config.colors.colorsConfig import COLORS
from config.config import *

#? parts
from components.app import app
from components.turing.rules import Rules



#? running states
class RunningState(Enum):
    RUNNING = "run"
    STOPPED = "stop"
    PAUSED  = "pause"
    FINISHED  = "finished"

@dataclass
class State:
    stop: str = "q0"
    active: str = "q1"

state = State()


class Tape:
    _instance = None

    head_position: int = TAPE.cells // 2 # center of the tape 
    symbols: list[str] = [TAPE.cell_sign] * TAPE.cells
    
    cells: list[CTkLabel] = []
    is_running: RunningState = RunningState.PAUSED

    state: str = TAPE.state

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            cls._instance.cells = []
            cls._instance.symbols = [TAPE.cell_sign] * TAPE.cells
            cls._instance.is_running = RunningState.PAUSED

            cls._instance.head_position = TAPE.cells // 2 
            cls._instance.state = TAPE.state

        return cls._instance


    def __init__(self):
        self.app = app

        #? parts
        self.Rules = Rules()


    def create_widgets(self):
        #? cells frame
        widgets.tape.cells_frame = XYFrame(
            self.app._app,
            height=TAPE.height,
            scrollbar_width=TAPE.scrollbar_height,
        )
        widgets.tape.cells_frame.grid(
            row=ROWS.cells,
            column=TAPE.first_column,
            columnspan=TAPE.last_column,
            padx=2,
            sticky="ew",
        )

        # ? alphabet label
        widgets.tape.alphabet_label = CTkLabel(
            self.app._app, text=f"{TEXTS.tape.alphabet_label}"
        )
        widgets.tape.alphabet_label.grid(
            row=ROWS.alphabet, column=0, padx=5, pady=(5)
        )

        # ? alphabet input
        widgets.tape.alphabet_input = CTkEntry(self.app._app, width=200)
        widgets.tape.alphabet_input.grid(
            row=ROWS.alphabet, column=1, columnspan=3, pady=20, padx=0, sticky="we"
        )
        widgets.tape.alphabet_input.insert(0, TAPE.alphabet)

        self.create_cells()

        # ? [set tape] signs button
        widgets.tape.buttons.set_tape_button = CTkButton(
            self.app._app, text=TEXTS.tape_buttons.set_tape, command=self.set_tape_symbols
        ).grid(row=ROWS.alphabet, column=4, padx=5, pady=5)

        #? arrow left
        widgets.tape.left_arrow = CTkButton(
            self.app._app, text=TEXTS.tape_buttons.left_arrow, width=ARROWS_CONFIG.width, height=ARROWS_CONFIG.height, fg_color=ARROWS_CONFIG.bg_color, command=lambda: widgets.tape.cells_frame.move_scrollbar(-ARROWS_CONFIG.move_size)
        ).grid(row=ROWS.arrows, column=0, padx=5, pady=5, sticky="w")
        
        #? arrow right
        widgets.tape.right_arrow = CTkButton(
            self.app._app, text=TEXTS.tape_buttons.right_arrow, width=ARROWS_CONFIG.width, height=ARROWS_CONFIG.height, fg_color=ARROWS_CONFIG.bg_color, command=lambda: widgets.tape.cells_frame.move_scrollbar(ARROWS_CONFIG.move_size)
        ).grid(row=ROWS.arrows, column=4, padx=5, pady=5, sticky="e")

        #? buttons
        widgets.tape.buttons_frame = CTkFrame(self.app._app, fg_color="transparent")
        widgets.tape.buttons_frame.grid(row=ROWS.tape_buttons, column=0, columnspan=5)
        
        #? left
        widgets.tape.buttons.move_left_button = CTkButton(
            widgets.tape.buttons_frame, text=TEXTS.tape_buttons.step_left, command=self.move_left
        ).grid(row=ROWS.tape_buttons, column=0, padx=5, pady=10)

        #? right
        widgets.tape.buttons.move_right_button = CTkButton(
            widgets.tape.buttons_frame, text=TEXTS.tape_buttons.step_right, command=self.move_right
        ).grid(row=ROWS.tape_buttons, column=1, padx=5, pady=5)

        #? step
        widgets.tape.buttons.step_button = CTkButton(
            widgets.tape.buttons_frame, text=TEXTS.tape_buttons.step, command=self.make_step
        ).grid(row=ROWS.tape_buttons, column=2, padx=5, pady=5)

        #? run
        widgets.tape.buttons.run_button = CTkButton(
            widgets.tape.buttons_frame, text=TEXTS.tape_buttons.run, command=self.run
        ).grid(row=ROWS.tape_buttons, column=3, padx=5, pady=5)

        #? pause
        widgets.tape.buttons.pause_button = CTkButton(
            widgets.tape.buttons_frame, text=TEXTS.tape_buttons.pause, command=self.pause
        ).grid(row=ROWS.tape_buttons, column=4, padx=5, pady=5)
        
        #? stop
        widgets.tape.buttons.stop_button = CTkButton(
            widgets.tape.buttons_frame, text=TEXTS.tape_buttons.stop, command=self.stop
        ).grid(row=ROWS.tape_buttons, column=5, padx=5, pady=5)




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
            cell_number_label.grid(row=ROWS.cell_numbers, column=i, padx=2)

        
        #? create tape cells
        for i in range(cells_len):
            #? cells
            cell_label = CTkLabel(
                widgets.tape.cells_frame,
                text=TAPE.cell_sign,
                width=20,
                font=("Courier", 14),
                fg_color=("white", COLORS.tape.cell),
                corner_radius=5,
            )
            cell_label.grid(row=ROWS.cells, column=i, padx=2)
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

        label.grid(row=ROWS.cells, column=new_cell_position, padx=2)

        self.create_cells()
        self.set_tape_symbols()


    def set_tape_symbols(self):
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

        self.update_cells()


    # ? update cells color and symbol
    def update_cells(self) -> None:
        for i, symbol in enumerate(self.symbols):
            if i == self.head_position:
                self.cells[i].configure(fg_color=COLORS.tape.highlight)
            else:
                self.cells[i].configure(fg_color=("white", COLORS.tape.cell))
            self.cells[i].configure(text=symbol)

        self.update_ui_state()
        

    def update_cell(self, index: int, new_symbol: str) -> None:
        self.cells[index].configure(text=new_symbol)
        self.symbols[index] = new_symbol


    def update_ui_state(self) -> None:
        widgets.tape.state_label.configure(text=f"{TEXTS.tape.state_label}: {self.state}")


    def run(self) -> None:
        self.is_running = RunningState.RUNNING
        self.set_active_state()
        self.run_until_stop()


    def pause(self) -> None:
        self.is_running = RunningState.PAUSED
        self.update_ui_state()


    def stop(self) -> None:
        """ stops tape from running, prepares active state """
        self.is_running = RunningState.STOPPED
        self.state = state.active
        self.update_ui_state()
        self.app.open_stop_modal()


    def finish(self) -> None:
        """ opens modal, sets state to active manually """
        self.update_cells()
        self.update_ui_state()
        # self.app.open_finish_modal()
        self.app.open_finish_modal()


    def run_until_stop(self) -> None:
        #? run
        if (
            self.is_running == RunningState.RUNNING
            and (self.state, self.symbols[self.head_position]) in self.Rules.rules
        ):
            self.make_step()
            self.app._app.after(500, self.run_until_stop)
            
        #? pause
        elif self.is_running == RunningState.PAUSED:
            self.pause()
        
        #? or stop
        elif self.is_running == RunningState.STOPPED:
            self.stop()

        else: 
            self.finish()


    def set_active_state(self) -> None:
        if self.state == state.stop:
            self.state = state.active
            self.update_ui_state()
        self.is_running = RunningState.RUNNING 


    def make_step(self) -> None:
        self.set_active_state()
        self.Rules.read_rules()
        
        current_symbol = self.symbols[self.head_position]

        if (self.state, current_symbol) in self.Rules.rules:
            next_state, write_symbol, direction = self.Rules.rules[(self.state, current_symbol)]

            self.symbols[self.head_position] = write_symbol
            self.state = next_state

            #? finish algorithm
            if self.state == state.stop:
                self.is_running = RunningState.FINISHED
                self.finish()
                return

            else:
                self.move_cursor(direction) #? (L, R, S )
                self.update_cells()


    #? move in direction
    def move_cursor(self, direction: str) -> None:
        if direction == "L":
            self.move_left()

        if direction == "R":
            self.move_right()
        
        if direction == "S":
            self.dont_move()
        

    def dont_move(self) -> None:
        self.update_cells()
        

    def move_left(self) -> None:
        if self.head_position > 0:
            self.head_position -= 1
            self.update_cells()


    def move_right(self) -> None:
        if self.head_position < len(self.symbols) - 1:
            self.head_position += 1
            self.update_cells()

    
    def clear_cells(self) -> None:
        for i, cell in enumerate(self.cells):
            self.symbols[i] = "_"
            cell.configure(text="_")

    def clear_alphabet(self) -> None:
        widgets.tape.alphabet_input.delete(0, END)
