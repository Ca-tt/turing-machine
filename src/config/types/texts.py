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
    set_tape: str
    step: str
    step_left: str
    step_right: str
    run: str
    stop: str
    new_rule: str
    left_arrow: str = "<"
    right_arrow: str = ">"

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
