from dataclasses import dataclass, field
from typing import Literal, List
from custom_types.texts import *

# UI
@dataclass
class ButtonSize:
    width: int
    height: int
    padx: int
    pady: int


@dataclass
class Navbar:
    buttons: ButtonSize


@dataclass
class ColumnRange:
    start: int
    end: int


@dataclass
class Scrollbar:
    height: int
    left_shift: int


@dataclass
class TapeUI:
    height: int
    column: ColumnRange
    scrollbar: Scrollbar


@dataclass
class Rows:
    navbar: int
    description: int
    input_row: int
    tape: int
    buttons_row: int
    rules: int
    new_rule_button: int
    state_label: int


@dataclass
class UIConfig:
    theme: Literal["dark", "light"]
    colors: Literal["green", "blue", "dark-blue"]
    app_size: str
    title: str
    rows: Rows
    navbar: Navbar
    tape: TapeUI


# TAPE
@dataclass
class TapeConfig:
    sign: str
    position: int
    input: str
    cells: int
    state: str
    rules: List[str] = field(default_factory=list)


# COLORS
@dataclass
class TapeColors:
    cell: str
    highlight: str


@dataclass
class NavbarColors:
    background: str
    buttons: str


@dataclass
class ColorsConfig:
    tape: TapeColors
    navbar: NavbarColors
