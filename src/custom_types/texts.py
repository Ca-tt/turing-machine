from dataclasses import dataclass, field
from config.texts.ErrorTexts import *

@dataclass
class NavbarTexts:
    save_as_button: str = "Зберегти як.."
    open_file_button: str = "Вiдкрити.."
    close_app_button: str = "Закрити"

@dataclass
class DescriptionText:
    label: str = "Умова задачi:"


@dataclass
class TapeTexts:
    alphabet_label: str = "Алфавiт:"
    state_label: str = "Активний стан:"


@dataclass
class TapeButtonTexts:
    set_tape_button: str
    step_button: str
    step_left_button: str
    step_right_button: str
    run_button: str
    stop_button: str
    new_rule_button: str

@dataclass
class RulesTexts:
    label: str = "Правила:"

@dataclass
class CommentsTexts:
    label: str = "Коментарi:"


#? modals
@dataclass
class ModalTexts:
    save_to_file_modal_title: str = "Зберегти данi.."
    open_file_modal_title: str = "Вiдкрити файл.."


#? final texts config
@dataclass
class TextConfig:
    navbar: NavbarTexts
    task_description: DescriptionText
    button: TapeButtonTexts
    errors: ErrorText
    tape: TapeTexts
    modals: ModalTexts
    comments: CommentsTexts
    rules: RulesTexts
