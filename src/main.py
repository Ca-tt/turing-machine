from customtkinter import (
    CTk,
    CTkButton,
    CTkFrame,
    CTkLabel,
)

# ? configs
from ui.config import UI, TAPE, TEXT, COLORS

# ? UI
from ui.widgets import widgets

#? parts
from ui.app import App, app
from turing.tape import Tape
from turing.rules import Rules
from file_saver import FileSaver


class TuringMachineApp:
    def __init__(self):
        # ? classes
        self.Rules = Rules()
        self.Tape = Tape()

        self.FileSaver = FileSaver()
        self.FileSaver.create_widgets()

        #? UI
        # self.create_widgets()

        #? widgets
        self.Tape.create_widgets()
        self.Rules.create_widgets()

        #? set data
        self.Rules.read_rules()
        self.Tape.set_symbols()



    # def create_widgets(self):
    #     # ? [navbar] buttons
    #     # ? save
    #     widgets["navbar"]["buttons"]["save_to_file"] = CTkButton(
    #         widgets["navbar"]["frame"],
    #         text="Save",
    #         fg_color=COLORS["navbar"]["buttons"],
    #         height=UI["navbar"]["buttons"]["height"],
    #         width=UI["navbar"]["buttons"]["width"],
    #         command=self.FileSaver._save_to_file,
    #     ).grid(
    #         row=UI["rows"]["navbar"],
    #         column=0,
    #         padx=UI["navbar"]["buttons"]["padx"],
    #         pady=0,
    #     )

    #     # ? load
    #     widgets["navbar"]["buttons"]["load_from_file"] = CTkButton(
    #         widgets["navbar"]["frame"],
    #         text="Load",
    #         fg_color=COLORS["navbar"]["buttons"],
    #         height=UI["navbar"]["buttons"]["height"],
    #         width=UI["navbar"]["buttons"]["width"],
    #         command=self.FileSaver._load_from_file,
    #     ).grid(
    #         row=UI["rows"]["navbar"],
    #         column=1,
    #         padx=UI["navbar"]["buttons"]["padx"],
    #         pady=0,
    #     )





if __name__ == "__main__":
    app.set_ui_settings()
    app.place_widgets()

    #? create interface with all functions    
    turing_machine = TuringMachineApp()

    #? runs the window
    app.open()
