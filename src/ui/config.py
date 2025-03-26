from custom_types.configT import *

# settings
UI: UIConfig = {
    "theme": "light",  # dark, light
    "colors": "green",  # green, blue, dark-blue
    "size": "750x480",
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
    "position": 1,
    "state": "q0",
    "input": "123",
    "cells": 5,
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
        "set_tape": "Завантажити стрiчку",
        "step": "Крок",
        "step_left": "← Влiво",
        "step_right": "Вправо →",
        "run": "Запустити",
        "stop": "Зупинит",
        "new_rule": "Додати нове правило",
    },
    "errors": {
        "tape": {
            "input": {
                "too_many_symbols": "You've entered too many symbols, please shorten your input or add additional cells",
            }
        },
        "rules": {
            "invalid_rule": f"You rule is uncorrect, please double check it: "
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
