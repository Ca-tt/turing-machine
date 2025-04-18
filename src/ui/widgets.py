from dataclasses import dataclass, field
from typing import Optional

from customtkinter import CTkButton, CTkEntry, CTkFrame, CTkLabel

#? custom widgets
from ui.scrollable_frame import VerticalScrollableFrame
from ui.xy_frame import XYFrame


@dataclass
class NavbarButtons:
    save_to_file: Optional[CTkButton] = None
    load_from_file: Optional[CTkButton] = None
    close_app: Optional[CTkButton] = None


@dataclass
class TapeButtons:
    set_tape_text: Optional[CTkButton] = None
    move_left: Optional[CTkButton] = None
    move_right: Optional[CTkButton] = None
    step: Optional[CTkButton] = None
    run: Optional[CTkButton] = None
    stop: Optional[CTkButton] = None


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
    symbols_input: Optional[CTkEntry] = None
    buttons: TapeButtons = field(default_factory=TapeButtons)
    cells: list[CTkLabel] = field(default_factory=list)
    state_label: Optional[CTkLabel] = None


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
