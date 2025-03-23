from re import sub

from customtkinter import (
    CTk,
    CTkButton,
    CTkEntry,
    CTkFrame,
    CTkLabel,
    set_appearance_mode,
    set_default_color_theme,
)

# ? configs
from ui.config import UI, TAPE, TEXT, COLORS

# ? UI
from ui.widgets import widgets
from ui.scrollable_frame import VerticalScrollableFrame
from ui.xy_frame import XYFrame

#? parts
from file_saver import FileSaver
from turing.tape import Tape


class TuringMachineApp:
    def __init__(self, root: CTk):
        self.app = root

        # ? classes
        self.Tape = Tape(self.app)

        self.rules: dict[str, tuple[str, str]] = {} # (read_state, value) = (write_state, value)
        self.rule_fields: list[CTkEntry] = []

        self.FileSaver = FileSaver()

        # set UI
        self.set_ui_settings()
        self.create_widgets()

        # update UI
        self.Tape.create_widgets()
        self.Tape.update_cells()
        self.read_rules()
        self.Tape.set_cells_text()

    def set_ui_settings(self):
        set_appearance_mode(UI["theme"])
        set_default_color_theme(UI["colors"])

        self.app.title(UI["title"])
        self.app.geometry(UI["size"])

        self.app.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

    def create_widgets(self):
        # ? [navbar]
        widgets["navbar"]["frame"] = CTkFrame(self.app, fg_color=COLORS["navbar"]["background"])
        widgets["navbar"]["frame"].grid(row=UI["rows"]["navbar"], column=0, columnspan=6, sticky="ew")

        # ? [navbar] buttons
        # ? save
        widgets["navbar"]["buttons"]["save_to_file"] = CTkButton(
            widgets["navbar"]["frame"],
            text="Save",
            fg_color=COLORS["navbar"]["buttons"],
            height=UI["navbar"]["buttons"]["height"],
            width=UI["navbar"]["buttons"]["width"],
            command=self.FileSaver._save_to_file,
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
            command=self.FileSaver._load_from_file,
        ).grid(
            row=UI["rows"]["navbar"],
            column=1,
            padx=UI["navbar"]["buttons"]["padx"],
            pady=0,
        )

        # ? quit
        widgets["navbar"]["buttons"]["close_app"] =CTkButton(
            widgets["navbar"]["frame"],
            text="Exit",
            fg_color=COLORS["navbar"]["buttons"],
            height=UI["navbar"]["buttons"]["height"],
            width=UI["navbar"]["buttons"]["width"],
            command=self.app.destroy,
        ).grid(
            row=UI["rows"]["navbar"],
            column=2,
            padx=UI["navbar"]["buttons"]["padx"],
            pady=0,
        )


        # ? vertical frame
        widgets["rules"]["frame"] = VerticalScrollableFrame(self.app)
        widgets["rules"]["frame"].grid(row=UI["rows"]["rules"], column=0, columnspan=5, pady=10)

        # ? [new rule] button
        widgets["rules"]["add_rule_button"] = CTkButton(
            self.app,
            text=TEXT["button"]["new_rule"],
            command= widgets["rules"]["frame"].add_new_input_widget,
        ).grid(row=UI["rows"]["new_rule_button"], column=0, columnspan=5, pady=5)

        widgets["tape"]["state"] = CTkLabel(self.app, text=f"State: {self.Tape.state}")
        widgets["tape"]["state"].grid(
            row=UI["rows"]["state_label"], column=0, columnspan=5, pady=5
        )


    # ? goes through rules entries and get rules data
    def read_rules(self):
        self.rules.clear()

        self.rule_fields =  widgets["rules"]["frame"].get_widgets()
        # print("rule fields:", len(self.rule_entries))

        for entry in self.rule_fields:
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
                print(f"Invalid rule format: {rule_text}")




if __name__ == "__main__":
    root = CTk()
    app = TuringMachineApp(root)
    root.mainloop()
