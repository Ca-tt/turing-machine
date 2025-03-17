import customtkinter as ctk
from configs import UI, TAPE


class TuringMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title(UI["title"])
        self.root.geometry(UI["size"])

        ctk.set_appearance_mode(UI["theme"])
        ctk.set_default_color_theme(UI["colors"])

        self.tape = [TAPE["sign"]] * 21
        self.head_position = TAPE["position"]
        self.state = "q0"
        self.rules = {}
        self.is_tape_running = False
        self.rule_entries = []

        self.create_widgets()

        # update the UI
        self.update_tape_display()

        self.predefine_rules()
        self.read_rules()

        self.set_tape()

    def create_widgets(self):
        self.input_entry = ctk.CTkEntry(self.root, width=200)
        self.input_entry.grid(row=0, column=0, columnspan=3, pady=5)
        self.input_entry.insert(0, TAPE["input"])

        ctk.CTkButton(self.root, text="Set Tape", command=self.set_tape).grid(
            row=0, column=3, padx=5, pady=5
        )

        self.tape_frame = ctk.CTkFrame(self.root)
        self.tape_frame.grid(row=1, column=0, columnspan=5, pady=5)
        self.tape_labels = []

        for i in range(21):
            label = ctk.CTkLabel(
                self.tape_frame,
                text="_",
                width=20,
                font=("Courier", 14),
                fg_color=("white", "gray20"),
                corner_radius=5,
            )
            label.grid(row=0, column=i, padx=2)
            self.tape_labels.append(label)

        ctk.CTkButton(self.root, text="← Left", command=self.move_left).grid(
            row=2, column=0, pady=5
        )
        ctk.CTkButton(self.root, text="Right →", command=self.move_right).grid(
            row=2, column=1, pady=5
        )
        ctk.CTkButton(self.root, text="Step", command=self.step).grid(
            row=2, column=2, pady=5
        )
        ctk.CTkButton(self.root, text="Run", command=self.run).grid(
            row=2, column=3, pady=5
        )
        ctk.CTkButton(self.root, text="Stop", command=self.stop).grid(
            row=2, column=4, pady=5
        )

        self.rules_frame = ctk.CTkFrame(self.root)
        self.rules_frame.grid(row=3, column=0, columnspan=5, pady=10)

        ctk.CTkButton(
            self.root, text="Add a New Rule", command=self.add_rule_input
        ).grid(row=4, column=0, columnspan=5, pady=5)

        self.status_label = ctk.CTkLabel(self.root, text=f"State: {self.state}")
        self.status_label.grid(row=5, column=0, columnspan=5, pady=5)

    def update_tape_display(self):
        for i, symbol in enumerate(self.tape):
            if i == self.head_position:
                self.tape_labels[i].configure(fg_color="yellow")
            else:
                self.tape_labels[i].configure(fg_color=("white", "gray20"))
            self.tape_labels[i].configure(text=symbol)
        self.status_label.configure(text=f"State: {self.state}")

    def set_tape(self):
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

    def add_rule_input(self):
        rule_entry = ctk.CTkEntry(self.rules_frame, width=300)
        rule_entry.pack(pady=2)
        self.rule_entries.append(rule_entry)

    def predefine_rules(self):
        for rule in TAPE["rules"]:
            rule_entry = ctk.CTkEntry(self.rules_frame, width=300)
            rule_entry.pack(pady=2)
            rule_entry.insert(0, rule)
            self.rule_entries.append(rule_entry)

    def read_rules(self):
        self.rules.clear()
        for entry in self.rule_entries:
            rule_text = entry.get().strip()
            try:
                parts = rule_text.split("->")
                left, right = parts[0].strip(), parts[1].strip()
                state, read_symbol = left.split(",")
                next_state, write_symbol, move = right.split(",")
                self.rules[(state, read_symbol)] = (next_state, write_symbol, move)
            except:
                print(f"Invalid rule format: {rule_text}")

    def step(self):
        self.read_rules()
        current_symbol = self.tape[self.head_position]
        if (self.state, current_symbol) in self.rules:
            next_state, write_symbol, move = self.rules[(self.state, current_symbol)]
            self.tape[self.head_position] = write_symbol
            self.state = next_state
            if move == "L":
                self.move_left()
            elif move == "R":
                self.move_right()
            self.update_tape_display()

    def run(self):
        self.is_tape_running = True
        self.execute()

    def stop(self):
        self.is_tape_running = False

    def execute(self):
        if (
            self.is_tape_running
            and (self.state, self.tape[self.head_position]) in self.rules
        ):
            self.step()
            self.root.after(500, self.execute)
        else:
            self.is_tape_running = False


if __name__ == "__main__":
    root = ctk.CTk()
    app = TuringMachineApp(root)
    root.mainloop()
