from dataclasses import dataclass, field
from typing import Literal, List
from config.types.texts import *

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
    start: int = 0
    end: int = 5


@dataclass
class Scrollbar:
    height: int = 13
    start_position: int = 8000



@dataclass
class TapeCellsConfig:
    height: int
    column: ColumnRange
    scrollbar: Scrollbar



# TAPE
@dataclass
class TapeConfig:
    cell_sign: str
    alphabet: str
    tape_input: str
    cells: int
    state: str
    rules: List[str] = field(default_factory=list[str])


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
