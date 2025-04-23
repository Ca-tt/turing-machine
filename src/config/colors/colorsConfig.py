from dataclasses import dataclass


# COLORS
@dataclass
class TapeColors:
    cell: str
    highlight: str


@dataclass
class NavbarColors:
    background: str
    buttons: str


@dataclass
class ColorsConfig:
    tape: TapeColors
    navbar: NavbarColors

COLORS = ColorsConfig(
    tape=TapeColors(cell="gray20", highlight="yellow"),
    navbar=NavbarColors(background="white", buttons="gray80"),
)

