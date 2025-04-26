from customtkinter import (
    CTkButton,
    CTkEntry,
    CTkLabel
)

# ? configs
# ? configs
from config.texts.texts import TEXTS
from config.colors.colorsConfig import COLORS
from config.config import ROWS

# ? UI
from components.widgets import widgets
from components.frames.scrollable_frame import VerticalScrollableFrame

#? parts
from components.app import App, app


class Rules:
    __rules_instance = None

    fields: list[CTkEntry] = []
    rules: dict[str, tuple[str, str]] = {}

    def __new__(cls, *args, **kwargs):
        if cls.__rules_instance is None:
            cls.__rules_instance = super().__new__(cls)
            cls.__rules_instance.fields = []
            cls.__rules_instance.rules = {}

        return cls.__rules_instance


    def __init__(self):
        self.app = app._app


    def create_widgets(self):
        #? vertical frame
        widgets.rules.frame = VerticalScrollableFrame(self.app)

        #? label
        widgets.rules.label = CTkLabel(
            self.app, text=f"{TEXTS.rules.label}"
        )
        widgets.rules.label.grid(
            row=ROWS.rules_comments_labels, column=1, padx=5, pady=(5)
        )

        #? rules fields 
        widgets.rules.frame.place_fields()
        widgets.rules.frame.grid(row=ROWS.rules_inputs, column=0, columnspan=3, pady=10, padx=20, sticky="we")

        #? make rule_fields accessible globally
        widgets.rules.inputs = widgets.rules.frame.get_fields()
        self.fields = widgets.rules.frame.get_fields()

        # ? [new rule] button
        widgets.rules.add_rule_button = CTkButton(
            self.app,
            text=TEXTS.tape_buttons.new_rule,
            command= widgets.rules.frame.add_new_field,
        ).grid(row=ROWS.new_rule_button, column=0, columnspan=3, padx=100, pady=5, sticky="we")


    def get_rules(self):
        return self.rules
    

    def get_fields(self):
        return self.fields


    def set_rules(self, new_rules):
        self.rules = new_rules

    def clear_rules(self):
        self.rules = {}

    def clear_inputs(self):
        for input in widgets.rules.inputs:
            input.delete(0, "end")
            input.insert(0, "")


    def remove_inputs(self):
        for input in widgets.rules.inputs:
            input.grid_remove()
            
        widgets.rules.inputs = []


    def read_rules(self):
        self.rules.clear()

        for entry in self.fields:
            if entry.get() != "":
                rule_text = entry.get().strip()

                try:
                    parts = rule_text.split(">")
                    left = parts[0].strip()
                    right = parts[1].strip()

                    state, read_symbol = left.split(",")

                    # ? Split right-hand side by commas
                    right_parts = right.split(",")

                    if len(right_parts) == 3:
                        next_state, write_symbol, move = right_parts
                    elif len(right_parts) == 2:
                        next_state, write_symbol = right_parts
                        move = "S" # it is unneccessary, but let it be by default 
                    else:
                        raise ValueError("Invalid rule format")

                    self.rules[(state.strip(), read_symbol.strip())] = (
                        next_state.strip(), write_symbol.strip(), move
                    )
                except Exception as e:
                    print(f"{TEXTS.errors.invalid_rule.invalid_rule} {rule_text} ({e})")

        return self.rules

