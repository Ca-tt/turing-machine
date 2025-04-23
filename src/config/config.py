from typing import Literal
from dataclasses import dataclass, field


# ?  app settings
@dataclass
class Rows:
    navbar: int = 0
    task_description_label: int = 1
    task_description_input: int = 2
    alphabet: int = 3
    arrows: int = 4
    cell_numbers: int = 5
    cells: int = 6
    tape_buttons: int = 7
    rules_comments_labels = 8
    rules_inputs: int = 9
    new_rule_button: int = 10
    state_label: int = 11


@dataclass
class APP_WINDOW:
    theme: Literal["dark", "light"] = "light"
    colors: Literal["green", "blue", "dark-blue"] = "green"
    title: str = "Машина Тьюрiнга"

    width: int = 800
    height: int = 700
    window_size: str = "800x700"
    offset_top: int = 0
    offset_left: int = 0


# UI
@dataclass
class Navbar:
    button_width: int = 50
    button_height: int = 20
    button_padx: int = 5
    button_pady: int = 0


@dataclass
class TapeConfig:
    cell_sign: str = "_"
    state: str = "q1"
    alphabet: str = "abcde"
    cells: int = 75
    rules: list[str] = field(default_factory=lambda: [
        "q1,a -> q2,b,R",
        "q1,b -> q2,a,R",
        "q2,a -> q3,b,R",
        "q2,b -> q3,a,R",
        "q3,a -> q0,b",
        "q3,b -> q0,a",
    ])

    first_column: int = 0
    last_column: int = 5
    height: int = 60
    scrollbar_height: int = 13
    scrollbar_offset_left: int = 8000


@dataclass
class DescriptionConfig:
    padx: int = 20
    input_height: int = 60


@dataclass
class CommentsConfig:
    padx: int = 20
    input_height: int = 60


@dataclass
class ArrowsConfig:
    padx: int = 20
    height: int = 40
    width: int = 40
    bg_color: str = "blue"
    move_size: int = 1


@dataclass
class SavedData:
    alphabet: str = ""
    rules: dict = field(default_factory=dict)
    task_conditions: str = ""
    comments: str = ""


# ? CONFIGS

ROWS = Rows()
NAVBAR = Navbar()
TAPE = TapeConfig()

APP_WINDOW = APP_WINDOW()

TASK_DESCRIPTION = DescriptionConfig()
COMMENTS = DescriptionConfig()
ARROWS_CONFIG = ArrowsConfig()
