from customtkinter import (
    CTkButton,
    CTkEntry,
)

# ? configs
from ui.config import UI, TAPE, TEXT, COLORS

# ? UI
from ui.widgets import widgets
from ui.scrollable_frame import VerticalScrollableFrame

#? parts
from ui.app import App, app


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
        # self.rules: dict[str, tuple[str, str]] = {} # (read_state, value) = (write_state, value)
        # self.fields: list[CTkEntry] = []


    def create_widgets(self):
        #? vertical frame
        widgets["rules"]["frame"] = VerticalScrollableFrame(self.app)
        #? rules fields
        widgets["rules"]["frame"].place_fields()
        widgets["rules"]["frame"].grid(row=UI["rows"]["rules"], column=0, columnspan=5, pady=10)

        # make rule_fields accessible globally
        widgets["rules"]["fields"] = widgets["rules"]["frame"].get_fields()
        self.fields = widgets["rules"]["frame"].get_fields()

        # ? [new rule] button
        widgets["rules"]["add_rule_button"] = CTkButton(
            self.app,
            text=TEXT["button"]["new_rule"],
            command= widgets["rules"]["frame"].add_new_field,
        ).grid(row=UI["rows"]["new_rule_button"], column=0, columnspan=5, pady=5)


    def get_rules(self):
        return self.rules
    

    def get_fields(self):
        return self.fields


    def set_rules(self, new_rules):
        self.rules = new_rules


    # ? goes through rules entries and get rules data
    def read_rules(self):
        self.rules.clear()
        # print("🚀 ~ self.fields:", self.fields)

        for entry in self.fields:
            if entry.get() != "":
            # print("🐍  entry",entry)
                rule_text = entry.get().strip()

                # ? split left and right parts by '->'
                try:
                    parts = rule_text.split("->")

                    # ? make a [state] and a [read_symbol] from the left part
                    left = parts[0].strip()
                    state, read_symbol = left.split(",")

                    # ? make a [next_state] and [write_symbol] from the right part
                    right = parts[1].strip()
                    next_state, write_symbol, move = right.split(",")

                    # ? tuple will save only unique values
                    self.rules[(state, read_symbol)] = (next_state, write_symbol, move)
                    # print("🐍 self.rules (tuples)", self.rules)
                except:
                    print(f"{TEXT['errors']['rules']['invalid_rule']} {rule_text}")
        
        return self.rules
