import tkinter as tk


DEFAULT_INPUT = "10101010"
PREDEFINED_RULES = [
    "q0,0 -> q1,1,R",
    "q0,1 -> q1,0,R",
    "q1,0 -> q0,1,R",
    "q1,1 -> q0,0,R",
    "q0,_ -> q1,_,L",
]


class TuringMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Turing Machine Simulator")

        self.tape = ["_"] * 21  # Tape with blank symbols
        self.head_position = 10  # Head starts in the middle
        self.state = "q0"  # Initial state
        self.rules = {}  # Transition rules
        self.running = False  # Controls automatic execution
        self.rule_entries = []  # List of rule input fields

        self.create_widgets()
        self.update_tape_display()
        self.predefine_rules()
        self.read_rules()

    def create_widgets(self):
        # Entry field for tape input
        self.input_entry = tk.Entry(self.root, width=30)
        self.input_entry.grid(row=0, column=0, columnspan=3)
        self.input_entry.insert(0, DEFAULT_INPUT)

        tk.Button(self.root, text="Set Tape", command=self.set_tape).grid(
            row=0, column=3
        )

        # Tape display
        self.tape_frame = tk.Frame(self.root)
        self.tape_frame.grid(row=1, column=0, columnspan=5)
        self.tape_labels = []

        for i in range(21):
            label = tk.Label(
                self.tape_frame,
                text="_",
                width=3,
                font=("Courier", 14),
                relief=tk.SOLID,
            )
            label.grid(row=0, column=i)
            self.tape_labels.append(label)

        # Control buttons
        tk.Button(self.root, text="← Left", command=self.move_left).grid(
            row=2, column=0
        )
        tk.Button(self.root, text="Right →", command=self.move_right).grid(
            row=2, column=1
        )
        tk.Button(self.root, text="Step", command=self.step).grid(row=2, column=2)
        tk.Button(self.root, text="Run", command=self.run).grid(row=2, column=3)
        tk.Button(self.root, text="Stop", command=self.stop).grid(row=2, column=4)

        # Rule input section
        self.rules_frame = tk.Frame(self.root)
        self.rules_frame.grid(row=3, column=0, columnspan=5)

        # for _ in range(5):
        #     self.add_rule_input()

        tk.Button(self.root, text="Add a New Rule", command=self.add_rule_input).grid(
            row=4, column=0, columnspan=5
        )

        self.status_label = tk.Label(self.root, text=f"State: {self.state}")
        self.status_label.grid(row=5, column=0, columnspan=5)

    def update_tape_display(self):
        for i, symbol in enumerate(self.tape):
            if i == self.head_position:
                self.tape_labels[i]["bg"] = "yellow"
            else:
                self.tape_labels[i]["bg"] = "white"
            self.tape_labels[i]["text"] = symbol
        self.status_label.config(text=f"State: {self.state}")

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
        rule_entry = tk.Entry(self.rules_frame, width=40)
        rule_entry.pack()
        self.rule_entries.append(rule_entry)

    def predefine_rules(self):
        for rule in PREDEFINED_RULES:
            rule_entry = tk.Entry(self.rules_frame, width=40)
            rule_entry.pack()
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
        print("🐍 current_symbol", current_symbol)

        print("🐍 self.rules", self.rules)

        if (self.state, current_symbol) in self.rules:

            next_state, write_symbol, move = self.rules[(self.state, current_symbol)]

            self.tape[self.head_position] = write_symbol

            self.state = next_state
            if move == "L":
                self.move_left()
            elif move == "R":
                self.move_right()
            self.update_tape_display()
        else:
            print("No rule for this state and symbol!")

    def run(self):
        self.running = True
        self.execute()

    def stop(self):
        self.running = False

    def execute(self):
        print(
            "🐍 self.running",
            self.running,
        )

        if self.running:
            print("if")
            print("🐍 self.state", self.state)
            print("🐍 self.tape[self.head_position]", self.tape[self.head_position])

            print("🐍 self.rules", self.rules)
            if (self.state, self.tape[self.head_position]) in self.rules:
                print("if if")
                self.step()
                self.root.after(500, self.execute)  # Delay for visibility
            else:
                print("else")
                self.running = False  # Stop when no rule applies


if __name__ == "__main__":
    root = tk.Tk()
    app = TuringMachineApp(root)
    root.mainloop()
