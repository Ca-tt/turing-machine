from tkinter import END, filedialog
from re import sub
import json
from os.path import abspath, join, dirname

from customtkinter import CTkButton

# ? UI
from components import app
from components.widgets import widgets

# ? configs
from config.texts.texts import TEXTS
from config.colors.colorsConfig import COLORS
from config.config import *

#? parts
from components.turing.rules import Rules
from components.turing.tape import Tape


class FileSaver:
    def __init__(self, json_file_name="turing.json"):
        base_dir = dirname(abspath(__file__))
        files_dir = join(base_dir, "..", "files")

        self.default_file_path = join(files_dir, json_file_name)
        self.file_path = self.default_file_path

        self.app = app

        #? data to save
        self.saved_data = SavedData()

        #? parts
        self.Rules = Rules()
        self.Tape = Tape()


    def create_widgets(self):
        # ? new file button
        widgets.navbar.buttons.new_file = CTkButton(
            widgets.navbar.frame,
            text=TEXTS.navbar.new_file,
            fg_color=COLORS.navbar.buttons,
            height=NAVBAR.buttons_height,
            width=NAVBAR.buttons_width,
            command=self.reset_input_fields,
        ).grid(
            row=ROWS.navbar,
            column=0,
            padx=NAVBAR.button_padx,
            pady=0,
        )


        # ? save to file button
        widgets.navbar.buttons.save_to_file_button = CTkButton(
            widgets.navbar.frame,
            text=TEXTS.navbar.save_to_file,
            fg_color=COLORS.navbar.buttons,
            height=NAVBAR.buttons_height,
            width=NAVBAR.buttons_width,
            command=self.save_to_file,
        ).grid(
            row=ROWS.navbar,
            column=1,
            padx=NAVBAR.button_padx,
            pady=0,
        )

        widgets.navbar.buttons.open_file_button = CTkButton(
            widgets.navbar.frame,
            text=TEXTS.navbar.open_file,
            fg_color=COLORS.navbar.buttons,
            height=NAVBAR.buttons_height,
            width=NAVBAR.buttons_width,
            command=self.load_from_file,
        ).grid(
            row=ROWS.navbar,
            column=2,
            padx=NAVBAR.button_padx,
            pady=0,
        )

    def save_to_json(self):
        rules = self.Rules.read_rules()
        #? Convert tuple keys to strings
        self.saved_data.rules = {str(k): v for k, v in rules.items()}
        
        data = {
            "alphabet": self.saved_data.alphabet, 
            "rules": self.saved_data.rules,
            "conditions": self.saved_data.task_conditions,
            "comments": self.saved_data.comments
        }

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

            return data["alphabet"], rules_deserialized, data["conditions"], data["comments"]
        
        except Exception as e:
            print(f"Error loading file: {e}")
            return None, None

    def clear_saved_data(self):
        self.saved_data.alphabet = ""
        self.saved_data.rules = {}

    def save_to_file(self):
        #? conditions, comments
        self.saved_data.task_conditions = widgets.task_description.input.get("0.0", "end") 
        self.saved_data.comments = widgets.comments.input.get("0.0",  "end") 

        #? rules and alphabet
        self.saved_data.alphabet = widgets.tape.alphabet_input.get()
        self.Rules.read_rules()  # Update rules before saving

        # Ask the user for a file location
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All Files", "*.*")],
            title=TEXTS.modals.save_to_file_modal_title
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
            title=TEXTS.modals.open_file_modal_title
        )

        if file_path:
            self.file_path = file_path
            input_string, loaded_rules, task_conditions, comments = self.load_from_json()

            if task_conditions is not None:
                widgets.task_description.input.delete("0.0", "end")
                widgets.task_description.input.insert("0.0", task_conditions)
            
            if comments is not None:
                widgets.comments.input.delete("0.0", "end")
                widgets.comments.input.insert("0.0", comments)

            if input_string is not None:
                widgets.tape.alphabet_input.delete(0, "end")
                widgets.tape.alphabet_input.insert(0, input_string)

            # Handle loading rules into fields
            if loaded_rules is not None:
                self.Rules.clear_rules()
                self.Rules.clear_inputs()
                self.Rules.remove_inputs()

                loaded_rules_count = len(loaded_rules)
                fields_count = len(widgets.rules.inputs)

                # if loaded_rules_count > fields_count:
                for index in range(loaded_rules_count - fields_count):
                    new_input = widgets.rules.frame.add_new_field()
                    widgets.rules.inputs.append(new_input)
                    print("New field added! (on load json)")

                # Insert loaded rules into fields
                for index, (left_part, right_part) in enumerate(loaded_rules.items()):
                    regexp = r"['() ]"

                    old_state = sub(regexp, "", left_part[0])
                    read_value = sub(regexp, "", left_part[1])

                    new_state = right_part[0]
                    write_value = right_part[1]
                    direction = right_part[2]

                    rule_text = f"{old_state},{read_value} > {new_state},{write_value},{direction}"
                    widgets.rules.inputs[index].delete(0, "end")
                    widgets.rules.inputs[index].insert(0, rule_text)

                self.Tape.set_tape_symbols()
        else:
            print("Load operation canceled.")


    #? clear fields
    def reset_input_fields(self):
        self.Tape.clear_cells()
        self.Tape.clear_alphabet()
        
        self.Rules.clear_inputs()
        self.Rules.clear_rules()
        
        self.app.app.clear_textareas()
        
