from dataclasses import dataclass, field


@dataclass
class ModalConfig:
    title: str = ""
    width: int = 0
    height: int = 0
    size: str = ""


@dataclass
class AlphabetModal:
    title: str = "Обрати знак з алфавiту"
    width: int = 300
    height: int = 200
    size: str = f"{width}x{height}"
    left_offset: int = 0
    top_offset: int = 150

    cells_in_row: int = 6

@dataclass
class AboutAppModal:
    title: str = "Про програму"
    
    width: int = 600
    height: int = 350
    size: str = f"{width}x{height}"

    left_offset: int = 0
    top_offset: int = 0

@dataclass
class StopModal:
    title: str = "Програму зупинено"
    
    width: int = 280
    height: int = 100
    size: str = f"{width}x{height}"

    left_offset: int = 0
    top_offset: int = 0

@dataclass
class FinishModal:
    title: str = "Програма завершила роботу"
    
    width: int = 280
    height: int = 100
    size: str = f"{width}x{height}"

    left_offset: int = 0
    top_offset: int = 0


ALPHABET_MODAL_CONFIG = AlphabetModal()
ABOUT_APP_MODAL = AboutAppModal()

STOP_MODAL_CONFIG = StopModal()
FINIS_HMODAL_CONFIG = FinishModal()

