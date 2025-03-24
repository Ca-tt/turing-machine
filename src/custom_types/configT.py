from typing import TypedDict, Literal, Dict, List

class Rows(TypedDict):
    navbar: int
    input: int
    tape: int
    buttons: int
    rules: int
    new_rule_button: int
    state_label: int

class ButtonSize(TypedDict):
    width: int
    height: int
    padx: int
    pady: int

class Navbar(TypedDict):
    buttons: ButtonSize

class ColumnRange(TypedDict):
    start: int
    end: int

class Scrollbar(TypedDict):
    height: int
    left_shift: int

class TapeUI(TypedDict):
    height: int
    column: ColumnRange
    scrollbar: Scrollbar

class UIConfig(TypedDict):
    theme: Literal["dark", "light"]
    colors: Literal["green", "blue", "dark-blue"]
    size: str
    title: str
    rows: Rows
    navbar: Navbar
    tape: TapeUI

class TapeConfig(TypedDict):
    sign: str
    position: int
    input: str
    cells: int
    rules: List[str]
    state: str

class ButtonText(TypedDict):
    set_tape: str
    step: str
    step_left: str
    step_right: str
    run: str
    stop: str
    new_rule: str

class TapeError(TypedDict):
    too_many_symbols: str

class RulesErrors(TypedDict):
    invalid_rule: str

class TapeErrors(TypedDict):
    input: TapeError

class ErrorMessages(TypedDict):
    tape: TapeErrors
    rules: RulesErrors

class TextConfig(TypedDict):
    button: ButtonText
    errors: ErrorMessages

class TapeColors(TypedDict):
    cell: str
    highlight: str

class NavbarColors(TypedDict):
    background: str
    buttons: str

class ColorsConfig(TypedDict):
    tape: TapeColors
    navbar: NavbarColors
