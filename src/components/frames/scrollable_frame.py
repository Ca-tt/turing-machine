from customtkinter import CTkScrollableFrame, CTkEntry, CTkBaseClass

# ? config
from config.config import TAPE_CONFIG


class VerticalScrollableFrame(CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.widgets = []
        self.widget_values = []

        self.fields: list[CTkEntry] = []


    def place_elements(self, elements):
        for i, element in enumerate(elements):
            element.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="we")


    #? rules inputs
    def place_fields(self):
        for i, rule in enumerate(TAPE_CONFIG.rules):
            widget = CTkEntry(self, width=300)
            widget.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="we")
            widget.insert(0, rule)
            self.widgets.append(widget)
            self.fields.append(widget)


    def add_new_field(self):
        widget = CTkEntry(self, width=300)
        widget.grid(row=len(self.widgets), column=0, padx=10, pady=(10, 0), sticky="we")
        self.widgets.append(widget)
        self.fields.append(widget)


    def get_widget_values(self):
        for widget in self.widgets:
            self.widget_values.append(widget.get())
        return self.widget_values
    
    def get_fields(self):
        return self.fields


    def get_widgets(self):
        return self.widgets
