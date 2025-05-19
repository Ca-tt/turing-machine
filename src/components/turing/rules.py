from pydoc import text
from customtkinter import (
    CTkButton,
    CTkEntry,
    CTkLabel
)

# ? configs
# ? configs
from config.texts.texts import TEXTS
from config.colors.colorsConfig import COLORS
from config.config import ROWS, TAPE

# ? UI
from components.widgets import widgets
from components.frames.scrollable_frame import VerticalScrollableFrame

#? parts
from components.app import App, app


class Rules:
    __rules_instance = None

    rules_inputs: list[CTkEntry] = []
    rules: dict[str, tuple[str, str]] = {}

    def __new__(cls, *args, **kwargs):
        if cls.__rules_instance is None:
            cls.__rules_instance = super().__new__(cls)
            cls.__rules_instance.rules_inputs = []
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

        for rule in TAPE.rules:
            widgets.rules.frame.add_new_field(text=rule)

        # widgets.rules.frame.place_fields()
        widgets.rules.frame.grid(row=ROWS.rules_inputs, column=0, columnspan=3, pady=10, padx=20, sticky="we")

        #? make rule_fields accessible globally
        self.update_rules()

        # ? [new rule] button
        widgets.rules.add_rule_button = CTkButton(
            self.app,
            text=TEXTS.tape_buttons.new_rule,
            command= widgets.rules.frame.add_new_field,
        ).grid(row=ROWS.new_rule_button, column=0, columnspan=3, padx=100, pady=5, sticky="we")

    def update_rules(self):
        widgets.rules.inputs = widgets.rules.frame.get_fields()
        self.rules_inputs = widgets.rules.frame.get_fields()

    def get_rules(self):
        return self.rules
    
    def get_fields(self):
        return self.rules_inputs

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
        self.clear_rules()


    def read_rules(self):
        self.rules.clear()
        self.update_rules()

        for entry in self.rules_inputs:
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
                        move = "S" 
                    
                    else:
                        raise ValueError("Invalid rule format")

                    self.rules[(state.strip(), read_symbol.strip())] = (
                        next_state.strip(), write_symbol.strip(), move
                    )
                    
                except Exception as e:
                    print(f"{TEXTS.errors.invalid_rule.invalid_rule} {rule_text} ({e})")

        # print("self.rules (read_rules): ", self.rules)
        return self.rules


    def remove_rules_inputs(self):
        for input in self.rules_inputs:
            input.grid_remove()
