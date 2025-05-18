from customtkinter import CTkScrollableFrame, CTkEntry, CTkButton


class VerticalScrollableFrame(CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.inputs: list[CTkEntry] = []

        self.add_buttons: list[CTkButton] = []
        self.remove_buttons: list[CTkButton] = []


    def place_elements(self, elements: list[CTkEntry]):
        for i, element in enumerate(elements):
            element.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="we")


    def add_plus_button(self, index: int, input: CTkEntry):
        add_button = CTkButton(
            self, 
            text="+",
            width=50,
            command=lambda: self.recreate_inputs(index=index, input=input, operation="add"),
        )
        self.add_buttons.append(add_button)
        add_button.grid(row=index, column=1, padx=10)

    

    def add_minus_button(self, index: int, input: CTkEntry):
        remove_button = CTkButton(
            self, 
            text="—",
            width=50,
            command=lambda: self.recreate_inputs(index=index, input=input, operation="remove"),
        )
        self.remove_buttons.append(remove_button)
        remove_button.grid(row=index, column=2, padx=10)



    def add_new_field(self, text: str = "") -> CTkEntry:
        """ adds new rule input to vertical frame """
        input_index = len(self.inputs)

        new_input = CTkEntry(self, width=300)
        new_input.insert(0, text)
        new_input.grid(row=input_index, column=0, padx=10, pady=(10, 0), sticky="we")
        
        self.add_plus_button(index=input_index, input=new_input)
        self.add_minus_button(index=input_index, input=new_input)
        
        self.inputs.append(new_input)
        return new_input


    def get_widget_values(self) -> list[str]:
        """ returns list of input values """
        widget_values = []
        for widget in self.inputs:
            widget_values.append(widget.get())

        return widget_values
    

    def recreate_inputs(self, 
        index: int, 
        input: CTkEntry, 
        operation="remove"
    ):
        """ creates inputs again, with input added or removed """
        temp_inputs = self.inputs
        
        for input, add_button, remove_button in zip(self.inputs, self.add_buttons, self.remove_buttons):
            input.grid_forget()
            add_button.grid_forget()
            remove_button.grid_forget()

        self.inputs = []
        self.add_buttons = []
        self.remove_buttons = []

        match operation:
            case "remove":
                temp_inputs.pop(index)

                for input in temp_inputs:
                    self.add_new_field(input.get())
            
            case "add":
                empty_input = CTkEntry(self, width=300)
                temp_inputs.insert(index+1, empty_input)

                for input in temp_inputs:
                    self.add_new_field(input.get())
        

    def get_fields(self):
        return self.inputs


    def get_widgets(self):
        return self.inputs
