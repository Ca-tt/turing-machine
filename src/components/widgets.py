from dataclasses import dataclass, field
from typing import Optional

from customtkinter import CTkButton, CTkEntry, CTkFrame, CTkLabel, CTkTextbox

#? custom widgets
from components.frames.scrollable_frame import VerticalScrollableFrame
from components.frames.xy_frame import XYFrame
from config.modals.modalConfigs import AboutAppModal


@dataclass
class NavbarButtons:
    new_file: Optional[CTkButton] = None
    save_to_file_button: Optional[CTkButton] = None
    open_file_button: Optional[CTkButton] = None
    about_app: Optional[CTkButton] = None
    close_app: Optional[CTkButton] = None



@dataclass
class TapeButtons:
    set_tape_button: Optional[CTkButton] = None
    move_left_button: Optional[CTkButton] = None
    move_right_button: Optional[CTkButton] = None
    step_button: Optional[CTkButton] = None
    run_button: Optional[CTkButton] = None
    pause_button: Optional[CTkButton] = None
    stop_button: Optional[CTkButton] = None


@dataclass
class NavbarWidgets:
    frame: Optional[CTkFrame] = None
    buttons: NavbarButtons = field(default_factory=NavbarButtons)


@dataclass
class DescriptionWidgets:
    label: Optional[CTkLabel] = None
    input: Optional[CTkTextbox] = None


@dataclass
class TapeWidgets:
    cells_frame: Optional[XYFrame] = None
    buttons_frame: Optional[CTkFrame] = None

    buttons: TapeButtons = field(default_factory=TapeButtons)
    cells: list[CTkLabel] = field(default_factory=list)
    
    alphabet_label: Optional[CTkLabel] = None
    alphabet_input: Optional[CTkEntry] = None
    state_label: Optional[CTkLabel] = None

    left_arrow: Optional[CTkButton] = None
    right_arrow: Optional[CTkButton] = None


@dataclass
class RulesWidgets:
    frame: Optional[VerticalScrollableFrame] = None
    label: Optional[CTkLabel] = None
    inputs: list[CTkEntry] = field(default_factory=list)
    add_rule_button: Optional[CTkButton] = None

class CommentsWidgets:
    input: Optional[CTkTextbox] = None
    label: Optional[CTkLabel] = None


#? modals
@dataclass
class AlphabetModalWidgets:
    frame: Optional[CTkFrame] = None
    cells: list[CTkLabel] = field(default_factory=list)

@dataclass
class AboutAppModalWidgets:
    frame: Optional[CTkFrame] = None
    textbox: Optional[CTkTextbox] = None

@dataclass
class StopModalWidgets:
    label: Optional[CTkLabel] = None

@dataclass
class FinishModalWidgets:
    label: Optional[CTkLabel] = None


@dataclass
class Widgets:
    navbar: NavbarWidgets = field(default_factory=NavbarWidgets)
    #? text fields
    task_description: DescriptionWidgets = field(default_factory=DescriptionWidgets)
    comments: CommentsWidgets = field(default_factory=CommentsWidgets)
    
    #? main components
    tape: TapeWidgets = field(default_factory=TapeWidgets)
    rules: RulesWidgets = field(default_factory=RulesWidgets)

    #? modals
    alphabetmodal: AlphabetModalWidgets = field(default_factory=AlphabetModalWidgets)
    aboutmodal: AboutAppModalWidgets = field(default_factory=AboutAppModalWidgets)
    stop_modal: StopModalWidgets = field(default_factory=StopModalWidgets)
    finish_modal: FinishModalWidgets = field(default_factory=FinishModalWidgets)
     



widgets = Widgets()
