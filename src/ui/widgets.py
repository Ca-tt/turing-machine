from typing import TypedDict
from customtkinter import CTkButton, CTkEntry, CTkFrame, CTkLabel
from ui.scrollable_frame import VerticalScrollableFrame
from ui.xy_frame import XYFrame


class NavbarWidgets(TypedDict):
    frame: XYFrame
    buttons: dict[str, CTkButton]


class TapeWidgets(TypedDict):
    frame: XYFrame
    symbols_input: CTkEntry
    buttons: dict[str, CTkButton]
    cells: list[CTkLabel]
    state: CTkEntry


class RulesWidgets(TypedDict):
    frame: VerticalScrollableFrame
    fields: list[CTkEntry]
    add_rule_button: CTkButton


class Widgets(TypedDict):
    navbar: NavbarWidgets
    tape: TapeWidgets
    rules: RulesWidgets


navbar_widgets: NavbarWidgets = {
    "frame": CTkFrame,
    "buttons": {
        "save_to_file": CTkButton,
        "load_from_file": CTkButton,
        "close_app": CTkButton,
    },
}

tape_widgets: TapeWidgets = {
    "frame": XYFrame,
    "input": CTkEntry,
    "buttons": {
        "set_tape_text": CTkButton,
        "move_left": CTkButton,
        "move_right": CTkButton,
        "step": CTkButton,
        "run": CTkButton,
        "stop": CTkButton,
    },
    "cells": [],  # List of CTkLabel instances
    "state": CTkLabel,
}

rules_widgets: RulesWidgets = {
    "frame": VerticalScrollableFrame,
    "fields": [],
    "add_rule_button": CTkButton,
}

widgets: Widgets = {
    "navbar": navbar_widgets,
    "tape": tape_widgets,
    "rules": rules_widgets,
}
