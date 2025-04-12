from tkinter import filedialog
from re import sub
import json
from os.path import abspath, join, dirname

from customtkinter import CTkButton

#? types
from custom_types.fileSaverT import *

# ? UI
from ui.widgets import widgets

# ? configs
from ui.config import UI, COLORS

#? parts
from turing.rules import Rules
from turing.tape import Tape


class FileSaver:
    def __init__(self, json_file_name="turing.json"):
        base_dir = dirname(abspath(__file__))
        files_dir = join(base_dir, "..", "files")

        self.default_file_path = join(files_dir, json_file_name)
        self.file_path = self.default_file_path

        #? data to save
        self.saved: SavedDataT = {
            "symbols": "",
            "rules": {},
        }

        #? parts
        self.Rules = Rules()
        self.Tape = Tape()

    def create_widgets(self):
        # ? [navbar] buttons
        widgets["navbar"]["buttons"]["save_to_file"] = CTkButton(
            widgets["navbar"]["frame"],
            text="Зберегти як..",
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

        widgets["navbar"]["buttons"]["load_from_file"] = CTkButton(
            widgets["navbar"]["frame"],
            text="Вiдкрити..",
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
        rules = self.Rules.read_rules()
        #? Convert tuple keys to strings
        self.saved["rules"] = {str(k): v for k, v in rules.items()}
        
        data = {"input": self.saved["symbols"], "rules": self.saved["rules"]}

        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
                print(f"Data successfully saved to {self.file_path}!")
                self.clear_saved_data()
        except Exception as e:
            print(f"Error saving file: {e}")

    def load_from_json(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            # Convert rule keys back to tuples
            rules_deserialized = {tuple(k.split(",")): v for k, v in data["rules"].items()}
            print(f"Data successfully loaded from {self.file_path}")

            return data["input"], rules_deserialized
        except Exception as e:
            print(f"Error loading file: {e}")
            return None, None

    def clear_saved_data(self):
        self.saved["symbols"] = ""
        self.saved["rules"] = {}

    def save_to_file(self):
        self.saved["symbols"] = widgets["tape"]["symbols_input"].get()
        self.Rules.read_rules()  # Update rules before saving

        # Ask the user for a file location
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All Files", "*.*")],
            title="Save Turing Machine Data"
        )

        if file_path:
            self.file_path = file_path
            self.save_to_json()
        else:
            print("Save operation canceled.")

    def load_from_file(self):
        # Ask the user to select a file to load
        file_path = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All Files", "*.*")],
            title="Load Turing Machine Data"
        )

        if file_path:
            self.file_path = file_path
            input_string, loaded_rules = self.load_from_json()

            if input_string is not None:
                widgets["tape"]["symbols_input"].delete(0, "end")
                widgets["tape"]["symbols_input"].insert(0, input_string)

            # Handle loading rules into fields
            if loaded_rules is not None:
                loaded_rules_count = len(loaded_rules)
                fields_count = len(widgets["rules"]["fields"])

                if loaded_rules_count > fields_count:
                    for index in range(loaded_rules_count - fields_count):
                        widgets["rules"]["frame"].add_new_field()
                        print("New field added! (on load json)")

                # Insert loaded rules into fields
                for index, (left_part, right_part) in enumerate(loaded_rules.items()):
                    regexp = r"['() ]"

                    old_state = sub(regexp, "", left_part[0])
                    read_value = sub(regexp, "", left_part[1])

                    new_state = right_part[0]
                    write_value = right_part[1]
                    direction = right_part[2]

                    rule_text = f"{old_state},{read_value} -> {new_state},{write_value},{direction}"
                    widgets["rules"]["fields"][index].delete(0, "end")
                    widgets["rules"]["fields"][index].insert(0, rule_text)

                self.Tape.set_symbols()
        else:
            print("Load operation canceled.")
