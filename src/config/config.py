from config.types.configT import *
from dataclasses import dataclass

#?  app settings
@dataclass
class Rows:
    navbar: int = 0
    task_description_label: int = 1
    task_description_input: int = 2
    alphabet: int = 3
    arrows: int = 4
    cell_numbers: int = 5
    cells: int = 6
    tape_buttons: int = 7
    rules_comments_labels = 8 
    rules_inputs: int = 9
    new_rule_button: int = 10
    state_label: int = 11


@dataclass
class UIConfig:
    theme: Literal["dark", "light"]
    colors: Literal["green", "blue", "dark-blue"]
    app_size: str
    title: str
    rows: Rows
    navbar: Navbar
    tape_cells: TapeCellsConfig



@dataclass
class DescriptionConfig:
    padx: int = 20
    input_height: int = 60 

@dataclass
class CommentsConfig:
    padx: int = 20
    input_height: int = 60 

@dataclass
class ArrowsConfig:
    padx: int = 20
    height: int = 40 
    width: int = 40
    bg_color: str = "blue" 
    move_size: int = 1


UI = UIConfig(
    theme="light",
    colors="green",
    app_size="800x700",
    title="Машина Тюрiнга",
    rows=Rows(),
    navbar=Navbar(buttons=ButtonSize(width=50, height=20, padx=5, pady=0)),
    tape_cells=TapeCellsConfig(
        height=60,
        column=ColumnRange(),
        scrollbar=Scrollbar(),
    ),
)

TASK_DESCRIPTION = DescriptionConfig()
COMMENTS = DescriptionConfig()
ARROWS_CONFIG = ArrowsConfig()

TAPE_CONFIG = TapeConfig(
    cell_sign="_",
    state="q1",
    alphabet="ab",
    tape_input="aaabbbbaa",
    cells=75,
    rules=[
        "q1,a -> q2,b,R",
        "q1,b -> q2,a,R",
        "q2,a -> q1,b,R",
        "q2,b -> q1,a,R",
    ],
)

TEXTS = TextConfig(
    navbar=NavbarTexts(),
    task_description=DescriptionText(label="Умови задачi:"),
    button=TapeButtonTexts(
        set_tape="Завантажити стрiчку",
        step="Крок",
        step_left="← Влiво",
        step_right="Вправо →",
        run="Запустити",
        stop="Зупинити",
        new_rule="Додати нове правило",
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
