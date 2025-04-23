from dataclasses import dataclass, field


@dataclass
class ModalConfig:
    title: str = ""
    width: int = 0
    height: int = 0
    size: str = ""


@dataclass
class AlphabetModalConfig:
    title: str = "Обрати знак з алфавiту"
    width: int = 300
    height: int = 300
    size: str = f"{width}x{height}"
    left_offset: int = 0
    top_offset: int = 150


ALPHABET_MODAL_CONFIG = AlphabetModalConfig()
