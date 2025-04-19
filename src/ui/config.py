from custom_types.configT import *

# settings
UI = UIConfig(
    theme="light",
    colors="green",
    app_size="750x550",
    title="Машина Тюрiнга",
    rows=Rows(
        navbar=0,
        description=1,
        input_row=2,
        tape=3,
        buttons_row=4,
        rules=5,
        new_rule_button=6,
        state_label=7,
    ),
    navbar=Navbar(buttons=ButtonSize(width=50, height=20, padx=5, pady=0)),
    tape=TapeUI(
        height=30,
        column=ColumnRange(start=1, end=3),
        scrollbar=Scrollbar(height=13, left_shift=450),
    ),
)

TAPE = TapeConfig(
    sign="_",
    position=1,
    state="q1",
    input="123",
    cells=5,
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
    description=DescriptionText(label="Умови задачi:"),
    button=ButtonText(
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
    modals=ModalTexts()
)

COLORS = ColorsConfig(
    tape=TapeColors(cell="gray20", highlight="yellow"),
    navbar=NavbarColors(background="white", buttons="gray80"),
)
