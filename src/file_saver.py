from re import sub
import json
from os.path import abspath, join, dirname

from customtkinter import (
    CTk,
    CTkButton,
    CTkEntry,
    CTkFrame,
    CTkLabel,
)

#? types
from custom_types.fileSaverT import *

# ? UI
from ui.widgets import widgets

# ? configs
from ui.config import UI, TAPE, TEXT, COLORS

#? parts
from turing.rules import Rules
from turing.tape import Tape


class FileSaver:
    def __init__(self, json_file_name="turing.json"):
        base_dir = dirname(abspath(__file__))
        files_dir = join(base_dir, "..", "files")

        self.file_path = join(files_dir, json_file_name)

        #? data to save
        self.saved: SavedDataT = {
            "symbols": "",
            "rules": {},
        }

        #? parts
        self.Rules = Rules()


    def create_widgets(self):
        # ? [navbar] buttons
        # ? save
        widgets["navbar"]["buttons"]["save_to_file"] = CTkButton(
            widgets["navbar"]["frame"],
            text="Save",
            fg_color=COLORS["navbar"]["buttons"],
            height=UI["navbar"]["buttons"]["height"],
            width=UI["navbar"]["buttons"]["width"],
            command=self.save_to_file,
        ).grid(
            row=UI["rows"]["navbar"],
            column=0,
            padx=UI["navbar"]["buttons"]["padx"],
            pady=0,
        )

        # ? load
        widgets["navbar"]["buttons"]["load_from_file"] = CTkButton(
            widgets["navbar"]["frame"],
            text="Load",
            fg_color=COLORS["navbar"]["buttons"],
            height=UI["navbar"]["buttons"]["height"],
            width=UI["navbar"]["buttons"]["width"],
            command=self.load_from_file,
        ).grid(
            row=UI["rows"]["navbar"],
            column=1,
            padx=UI["navbar"]["buttons"]["padx"],
            pady=0,
        )


    def save_to_json(self):
        # Convert tuple keys to strings
        self.saved["rules"] = {str(k): v for k, v in self.Rules.rules.items()}
        
        data = {"input": self.saved["symbols"], "rules": self.saved["rules"]}

        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
                print("data successfully saved!")
                self.clear_saved_data()
        except Exception as e:
            print(f"Error saving file: {e}")


    def load_from_json(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            # Convert rule keys back to tuples
            rules_deserialized = {tuple(k.split(",")): v for k, v in data["rules"].items()}

            return data["input"], rules_deserialized
        except Exception as e:
            print(f"Error loading data file (maybe it rules): {e}")
            return None, None
        

    def clear_saved_data(self):
        self.saved["rules"] = ""
        self.saved["symbols"] = {}
        

    def save_to_file(self):
        self.saved["symbols"] = widgets["tape"]["symbols_input"].get()
        # ? read rules to update self.rules
        self.Rules.read_rules()
        self.save_to_json()


    def load_from_file(self):
        input_string, loaded_rules = self.load_from_json()
        print("🐍 loaded symbols from json", input_string)
        print("🐍  loaded rules from json ", loaded_rules)

        if input_string is not None:
            # Set input field text
            widgets["tape"]["symbols_input"].delete(0, "end")
            widgets["tape"]["symbols_input"].insert(0, input_string)

        if loaded_rules is not None:
            # Set rules
            # self.Rules.rules = loaded_rules

            # Clear existing rule entries, set new texts for them

            # for i, string in enumerate()

            #! Тут есть проблемы со связкой Rules
            #! Поля Rules не обновляются после загрузки из JSON
            #! Почему-то пишет, что длина символов больше tape_lenght

            for entry, (left_part, right_part) in zip(
                self.Rules.rule_fields, loaded_rules.items()
            ):
                print("🐍 entry",entry)
                # print("🐍  key",left_part)
                # print("🐍  value",right_part)
                regexp = r"['() ]"

                old_state = sub(regexp, "", left_part[0])
                read_value = sub(regexp, "", left_part[1])

                new_state = right_part[0]
                write_value = right_part[1]

                direction = right_part[2]

                rule_text = (
                    f"{old_state},{read_value} -> {new_state},{write_value},{direction}"
                )
                entry.delete(0, "end")
                entry.insert(0, rule_text)

            Tape().set_cells_text()
