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
    height: int
    left_shift: int




@dataclass
class TapeUI:
    height: int
    column: ColumnRange
    scrollbar: Scrollbar






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
