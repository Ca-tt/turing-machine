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

class TapeErrors(TypedDict):
    input: TapeError

class ErrorMessages(TypedDict):
    tape: TapeErrors

class TextConfig(TypedDict):
    button: ButtonText
    erorrs: ErrorMessages

class TapeColors(TypedDict):
    cell: str
    highlight: str

class NavbarColors(TypedDict):
    background: str
    buttons: str

class ColorsConfig(TypedDict):
    tape: TapeColors
    navbar: NavbarColors


# settings
UI: UIConfig = {
    "theme": "dark",  # dark, light
    "colors": "green",  # green, blue, dark-blue
    "size": "750x450",
    "title": "Turing Machine (by Roman Gluschenko)",
    "rows": {
        "navbar": 0,
        "input": 1,
        "tape": 2,
        "buttons": 3,
        "rules": 4,
        "new_rule_button": 5,
        "state_label": 6,
    },
    "navbar": {
        "buttons": {
            "width": 50,
            "height": 20,
            "padx": 5,
            "pady": 0,
        }
    },
    "tape": {
        "height": 30,
        "column": {
            "start": 1,
            "end": 3,
        },
        "scrollbar": {"height": 13, "left_shift": 450},
    },
}

TAPE: TapeConfig = {
    "sign": "_",
    "position": 10,
    "input": "aba",
    "cells": 21,
    "rules": [
        "q0,a -> q1,b,R",
        "q0,b -> q1,a,R",
        "q1,a -> q0,b,R",
        "q1,b -> q0,a,R",
        "q0,_ -> q1,_,L",
    ],
}

TEXT: TextConfig = {
    "button": {
        "set_tape": "Set Tape",
        "step": "Step",
        "step_left": "← Left",
        "step_right": "Right →",
        "run": "Run",
        "stop": "Stop",
        "new_rule": "Add a New Rule",
    },
    "erorrs": {
        "tape": {
            "input": {
                "too_many_symbols": "You've entered too many symbols, please shorten your input or add additional cells",
            }
        }
    }
}

COLORS: ColorsConfig = {
    "tape": {
        "cell": "gray20",
        "highlight": "yellow",
    },
    "navbar": {
        "background": "white",
        "buttons": "gray80",
    },
}
