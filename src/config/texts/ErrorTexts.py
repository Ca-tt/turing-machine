from dataclasses import dataclass, field

#? Errors texts
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

