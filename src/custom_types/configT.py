from dataclasses import dataclass, field
from typing import Literal, List


# TEXT


@dataclass
class TapeTexts:
    state_label: str


@dataclass
class DescriptionText:
    label: str


@dataclass
class ButtonText:
    set_tape: str
    step: str
    step_left: str
    step_right: str
    run: str
    stop: str
    new_rule: str


@dataclass
class TapeError:
    too_many_symbols: str


@dataclass
class RulesErrors:
    invalid_rule: str


@dataclass
class TapeErrors:
    input: TapeError


@dataclass
class ErrorMessages:
    tape: TapeErrors
    rules: RulesErrors


@dataclass
class TextConfig:
    description: DescriptionText
    button: ButtonText
    errors: ErrorMessages
    tape: TapeTexts


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
    input: int
    tape: int
    buttons: int
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
