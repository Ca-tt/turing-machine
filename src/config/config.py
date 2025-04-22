from config.types.configT import *
from dataclasses import dataclass

#?  app settings
@dataclass
class Rows:
    navbar: int = 0
    task_description_label: int = 1
    task_description_input: int = 2
    alphabet: int = 3
    cell_numbers: int = 4
    cells: int = 5
    tape_buttons: int = 6
    rules_comments_labels = 7 
    rules_inputs: int = 8
    new_rule_button: int = 9
    state_label: int = 10


@dataclass
class UIConfig:
    theme: Literal["dark", "light"]
    colors: Literal["green", "blue", "dark-blue"]
    app_size: str
    title: str
    rows: Rows
    navbar: Navbar
    tape: TapeUI



@dataclass
class DescriptionConfig:
    padx: int = 20
    input_height: int = 60 

@dataclass
class CommentsConfig:
    padx: int = 20
    input_height: int = 60 


UI = UIConfig(
    theme="light",
    colors="green",
    app_size="780x630",
    title="Машина Тюрiнга",
    rows=Rows(),
    navbar=Navbar(buttons=ButtonSize(width=50, height=20, padx=5, pady=0)),
    tape=TapeUI(
        height=60,
        column=ColumnRange(),
        scrollbar=Scrollbar(height=13, left_shift=8300),
    ),
)

TASK_DESCRIPTION = DescriptionConfig()
COMMENTS = DescriptionConfig()

TAPE = TapeConfig(
    cell_sign="_",
    state="q1",
    alphabet="ab",
    tape_input="aaabbbbaa",
    cells=75,
    rules=[
        "q0,a -> q1,b,R",
        "q0,b -> q1,a,R",
        "q1,a -> q0,b,R",
        "q1,b -> q0,a,R",
        "q0,_ -> q1,_,L",
    ],
)

TEXTS = TextConfig(
    navbar=NavbarTexts(),
    task_description=DescriptionText(label="Умови задачi:"),
    button=TapeButtonTexts(
        set_tape_button="Завантажити стрiчку",
        step_button="Крок",
        step_left_button="← Влiво",
        step_right_button="Вправо →",
        run_button="Запустити",
        stop_button="Зупинити",
        new_rule_button="Додати нове правило",
    ),
    errors=ErrorText(
        tape=TapeErrorsText(
            input=TapeErrorText(
                too_many_symbols="You've entered too many symbols, please shorten your input or add additional cells"
            )
        ),
        rules=RulesErrorsText(
            invalid_rule="You rule is uncorrect, please double check it: "
        ),
    ),
    tape=TapeTexts(state_label="Активний стан"),
    modals=ModalTexts(),
    comments = CommentsTexts(),
    rules = RulesTexts(),
)

COLORS = ColorsConfig(
    tape=TapeColors(cell="gray20", highlight="yellow"),
    navbar=NavbarColors(background="white", buttons="gray80"),
)
