from customtkinter import (
    CTk,
    CTkButton,
    CTkEntry,
    CTkFrame,
    CTkLabel,
    set_appearance_mode,
    set_default_color_theme,
)
from file_saver import FileSaver
from ui.config import UI, TAPE, TEXT, COLORS
from ui.scrollable_frame import VerticalScrollableFrame
from re import sub


class TuringMachineApp:
    def __init__(self, root: CTk):
        self.app = root

        self.tape: list[str] = [TAPE["sign"]] * TAPE["cells"]
        self.head_position: int = TAPE["position"]

        self.state: str = "q0"
        self.rules: dict[str, tuple[str, str]] = {}

        self.is_tape_running = False
        self.rule_entries = []

        self.FileSaver = FileSaver()

        self.set_ui_settings()
        self.create_widgets()

        # update the UI
        self.update_tape_display()

        # self.predefine_rules()
        self.read_rules()

        self.set_tape_text()

    def set_ui_settings(self):
        set_appearance_mode(UI["theme"])
        set_default_color_theme(UI["colors"])

        self.app.title(UI["title"])
        self.app.geometry(UI["size"])

        self.app.grid_columnconfigure((0,1,2,3,4,5), weight=1)

    def create_widgets(self):
        # ? [navbar]
        self.navbar = CTkFrame(self.app, fg_color=COLORS["navbar"]["background"])
        self.navbar.grid(row=UI["rows"]["navbar"], column=0, columnspan=6, sticky="ew")

        # ? [navbar] buttons
        # ? save
        CTkButton(
            self.navbar,
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
        CTkButton(
            self.navbar,
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

        # ? quit
        CTkButton(
            self.navbar,
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

        # ? [input] field for numbers or characters
        self.input_entry = CTkEntry(self.app, width=200)
        self.input_entry.grid(row=UI["rows"]["input"], column=0, columnspan=3, pady=20)
        self.input_entry.insert(0, TAPE["input"])

        # ? [set tape] signs button
        CTkButton(
            self.app, text=TEXT["button"]["set_tape"], command=self.set_tape_text
        ).grid(row=UI["rows"]["input"], column=3, padx=5, pady=5)

        self.tape_frame = CTkFrame(self.app)
        self.tape_frame.grid(row=UI["rows"]["tape"], column=0, columnspan=5, pady=10)
        self.tape_labels = []

        # ? create tape cells
        for i in range(TAPE["cells"]):
            label = CTkLabel(
                self.tape_frame,
                text=TAPE["sign"],
                width=20,
                font=("Courier", 14),
                fg_color=("white", COLORS["tape"]["cell"]),
                corner_radius=5,
            )
            label.grid(row=UI["rows"]["tape"], column=i, padx=2)
            self.tape_labels.append(label)

        # ? step [left] / [right] buttons
        CTkButton(
            self.app, text=TEXT["button"]["step_left"], command=self.move_left
        ).grid(row=UI["rows"]["buttons"], column=0, pady=5)

        CTkButton(
            self.app, text=TEXT["button"]["step_right"], command=self.move_right
        ).grid(row=UI["rows"]["buttons"], column=1, pady=5)

        # ? [step], [run], [stop] butons
        CTkButton(self.app, text=TEXT["button"]["step"], command=self.make_step).grid(
            row=UI["rows"]["buttons"], column=2, pady=5
        )

        CTkButton(self.app, text=TEXT["button"]["run"], command=self.run).grid(
            row=UI["rows"]["buttons"], column=3, pady=5
        )

        CTkButton(self.app, text=TEXT["button"]["stop"], command=self.stop).grid(
            row=UI["rows"]["buttons"], column=4, pady=5
        )

        # self.rules_frame = CTkFrame(self.app)
        self.rules_frame = VerticalScrollableFrame(self.app)
        self.rules_frame.grid(row=UI["rows"]["rules"], column=0, columnspan=5, pady=10)

        # ? [new rule] button
        CTkButton(
            self.app, text=TEXT["button"]["new_rule"], command=self.rules_frame.add_new_input_widget
        ).grid(row=UI["rows"]["new_rule_button"], column=0, columnspan=5, pady=5)

        self.status_label = CTkLabel(self.app, text=f"State: {self.state}")
        self.status_label.grid(
            row=UI["rows"]["state_label"], column=0, columnspan=5, pady=5
        )

    # ? update cells color and symbol
    def update_tape_display(self):
        for i, symbol in enumerate(self.tape):
            if i == self.head_position:
                self.tape_labels[i].configure(fg_color=COLORS["tape"]["highlight"])
            else:
                self.tape_labels[i].configure(
                    fg_color=("white", COLORS["tape"]["cell"])
                )

            self.tape_labels[i].configure(text=symbol)
        self.status_label.configure(text=f"State: {self.state}")

    def set_tape_text(self):
        input_text = self.input_entry.get()
        for i, char in enumerate(input_text):
            if i < len(self.tape):
                self.tape[self.head_position - len(input_text) // 2 + i] = char
        self.update_tape_display()

    def move_left(self):
        if self.head_position > 0:
            self.head_position -= 1
            self.update_tape_display()

    def move_right(self):
        if self.head_position < len(self.tape) - 1:
            self.head_position += 1
            self.update_tape_display()

    # def add_rule_input(self):
    #     rule_entry = CTkEntry(self.rules_frame, width=300)
    #     rule_entry.pack(pady=2)
    #     self.rule_entries.append(rule_entry)

    # def predefine_rules(self):
    #     for rule in TAPE["rules"]:
    #         rule_entry = CTkEntry(self.rules_frame, width=300)
    #         rule_entry.pack(pady=2)
    #         rule_entry.insert(0, rule)
    #         self.rule_entries.append(rule_entry)

    # ? goes through rules entries and get rules data
    def read_rules(self):
        self.rules.clear()

        self.rule_entries = self.rules_frame.get_widgets()
        # print("rule fields:", len(self.rule_entries))

        for entry in self.rule_entries:
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

    def make_step(self):
        self.read_rules()

        current_symbol = self.tape[self.head_position]

        if (self.state, current_symbol) in self.rules:
            # ? get (next state, write symbol, direction) tuple
            next_state, write_symbol, move = self.rules[(self.state, current_symbol)]

            # ? set next symbol for the new cell
            self.tape[self.head_position] = write_symbol

            # ? update the state
            self.state = next_state

            # ? move cursor right or left
            if move == "L":
                self.move_left()
            elif move == "R":
                self.move_right()

            self.update_tape_display()

    def run(self):
        self.is_tape_running = True
        self.run_until_stop()

    def stop(self):
        self.is_tape_running = False

    # ? make tape running infinitely
    def run_until_stop(self):
        if (
            self.is_tape_running
            and (self.state, self.tape[self.head_position]) in self.rules
        ):
            self.make_step()
            self.app.after(500, self.run_until_stop)
        else:
            self.is_tape_running = False

    # ? save / load from file logic wrappers
    def save_to_file(self):
        input_string = self.input_entry.get()
        # ? read rules to update self.rules
        self.read_rules()
        self.FileSaver.save_to_file(input_string, self.rules)

    def load_from_file(self):
        input_string, loaded_rules = self.FileSaver.load_from_file()
        print("🐍 input_string", input_string)
        print("🐍  loaded_rules ", loaded_rules)

        if input_string is not None:
            # Set input field text
            self.input_entry.delete(0, "end")
            self.input_entry.insert(0, input_string)

        if loaded_rules is not None:
            # Set rules
            self.rules = loaded_rules

            # Clear existing rule entries, set new texts for them
            for entry, (left_part, right_part) in zip(
                self.rule_entries, self.rules.items()
            ):
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

            self.set_tape_text()


if __name__ == "__main__":
    root = CTk()
    app = TuringMachineApp(root)
    root.mainloop()
