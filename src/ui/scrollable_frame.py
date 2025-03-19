from customtkinter import CTkScrollableFrame, CTkEntry, CTkBaseClass
from ui.config import TAPE


class VerticalScrollableFrame(CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.widgets: CTkBaseClass = []
        self.widget_values = []

        self.place_inputs()

    def place_elements(self, elements):
        for i, element in enumerate(elements):
            element.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")

    def place_inputs(self):
        for i, rule in enumerate(TAPE["rules"]):
            widget = CTkEntry(self, width=300)
            widget.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            widget.insert(0, rule)
            self.widgets.append(widget)

    def add_new_input_widget(self):
        widget = CTkEntry(self, width=300)
        widget.grid(row=len(self.widgets), column=0, padx=10, pady=(10, 0), sticky="w")
        self.widgets.append(widget)

    def get_widget_values(self):
        for widget in self.widgets:
            self.widget_values.append(widget.get())
        # print("🐍 self.widget_values", self.widget_values)
        return self.widget_values

    def get_widgets(self):
        return self.widgets

    # def get(self):
    #     checked_checkboxes = []
    #     for checkbox in self.checkboxes:
    #         if checkbox.get() == 1:
    #             checked_checkboxes.append(checkbox.cget("text"))
    #     return checked_checkboxes


# class App(CTk):
#     def __init__(self):
#         super().__init__()

#         self.title("my app")
#         self.geometry("400x220")
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_rowconfigure(0, weight=1)

#         values = ["value 1", "value 2", "value 3", "value 4", "value 5", "value 6"]
#         self.scrollable_checkbox_frame = VerticalScrollableFrame(
#             self, title="Values", elements=values
#         )
#         self.scrollable_checkbox_frame.grid(
#             row=0, column=0, padx=10, pady=(10, 0), sticky="nsew"
#         )

#         self.button = CTkButton(self, text="my button", command=self.button_callback)
#         self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

#     def button_callback(self):
#         print("checkbox_frame:", self.checkbox_frame.get())
#         print("radiobutton_frame:", self.radiobutton_frame.get())


# app = App()
# app.mainloop()
