from dataclasses import dataclass, field


@dataclass
class TapeTexts:
    state_label: str


@dataclass
class DescriptionText:
    label: str


@dataclass
class ButtonText:
    set_tape_button: str
    step_button: str
    step_left_button: str
    step_right_button: str
    run_button: str
    stop_button: str
    new_rule_button: str


@dataclass
class TapeErrorText:
    too_many_symbols: str


@dataclass
class RulesErrorsText:
    invalid_rule: str


@dataclass
class TapeErrorsText:
    input: TapeErrorText


@dataclass
class ErrorText:
    tape: TapeErrorsText
    rules: RulesErrorsText

@dataclass
class NavbarTexts:
    save_as_button: str = "Зберегти як.."
    open_file_button: str = "Вiдкрити.."

#? modals
@dataclass
class ModalTexts:
    save_to_file_modal_title: str = "Зберегти данi.."
    open_file_modal_title: str = "Вiдкрити файл.."


#? final texts config
@dataclass
class TextConfig:
    navbar: NavbarTexts
    description: DescriptionText
    button: ButtonText
    errors: ErrorText
    tape: TapeTexts
    modals: ModalTexts
