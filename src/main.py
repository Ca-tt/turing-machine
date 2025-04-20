#? parts
from components.app import app
from components.turing.tape import Tape
from components.turing.rules import Rules
from components.file_saver import FileSaver


class TuringMachineApp:
    def __init__(self):
        # ? classes
        self.Rules = Rules()
        self.Tape = Tape()

        self.FileSaver = FileSaver()
        self.FileSaver.create_widgets()

        # #? widgets
        self.Tape.create_widgets()
        self.Rules.create_widgets()

        # #? set data
        self.Rules.read_rules()
        self.Tape.set_symbols()



if __name__ == "__main__":
    app.set_ui_settings()
    app.place_widgets()

    #? create interface with all functions    
    turing_machine = TuringMachineApp()

    #? runs the window
    app.open()
