from dataclasses import dataclass, field
from typing import Optional

from customtkinter import CTkButton, CTkEntry, CTkFrame, CTkLabel

#? custom widgets
from ui.scrollable_frame import VerticalScrollableFrame
from ui.xy_frame import XYFrame


@dataclass
class NavbarButtons:
    save_to_file_button: Optional[CTkButton] = None
    open_file_button: Optional[CTkButton] = None
    close_app: Optional[CTkButton] = None


@dataclass
class TapeButtons:
    set_tape_button: Optional[CTkButton] = None
    move_left_button: Optional[CTkButton] = None
    move_right_button: Optional[CTkButton] = None
    step_button: Optional[CTkButton] = None
    run_button: Optional[CTkButton] = None
    stop_button: Optional[CTkButton] = None


@dataclass
class NavbarWidgets:
    frame: Optional[CTkFrame] = None
    buttons: NavbarButtons = field(default_factory=NavbarButtons)


@dataclass
class DescriptionWidgets:
    label: Optional[CTkLabel] = None
    field: Optional[CTkEntry] = None


@dataclass
class TapeWidgets:
    frame: Optional[XYFrame] = None
    buttons: TapeButtons = field(default_factory=TapeButtons)
    cells: list[CTkLabel] = field(default_factory=list)
    state_label: Optional[CTkLabel] = None
    symbols_input: Optional[CTkEntry] = None


@dataclass
class RulesWidgets:
    frame: Optional[VerticalScrollableFrame] = None
    fields: list[CTkEntry] = field(default_factory=list)
    add_rule_button: Optional[CTkButton] = None


@dataclass
class Widgets:
    navbar: NavbarWidgets = field(default_factory=NavbarWidgets)
    description: DescriptionWidgets = field(default_factory=DescriptionWidgets)
    tape: TapeWidgets = field(default_factory=TapeWidgets)
    rules: RulesWidgets = field(default_factory=RulesWidgets)


widgets = Widgets()
