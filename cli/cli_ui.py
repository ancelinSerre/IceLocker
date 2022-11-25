"""
Set of functions used to style the CLI
"""
from typing import Dict

from colorama import Fore

from cli import InvalidStrengthError

COLORS: Dict[str, str] = {
    "Very weak": Fore.LIGHTRED_EX,
    "Weak": Fore.RED,
    "Reasonable": Fore.BLUE,
    "Strong": Fore.GREEN,
    "Very strong": Fore.LIGHTGREEN_EX
}


def colorize_strength(strength: str):
    """
    Function used to colorize the strength string representation.
    (Red for very weak, Green for very strong)

    Arguments:
    strength -- password strength string representation (from very weak to very strong)
    """
    strength_color = COLORS.get(strength)
    if strength_color is None:
        raise InvalidStrengthError

    return strength_color + strength + Fore.WHITE


def show_password_strength(strength: str, entropy: float, colors=True) -> None:
    """
    Function used to show password strength from very weak to very strong.

    Arguments:
    strength -- password strength string representation (from very weak to very strong).
    entropy -- password entropy in bits.
    """
    if colors:
        colorized_strength = colorize_strength(strength)
        print(f"Strength: {colorized_strength} ; Entropy {entropy:.0f}")
    else:
        print(f"Strength: {strength} ; Entropy {entropy:.0f}")


def show_password(password: str, colors=True) -> None:
    """
    Function used to show password to user on CLI.

    Arguments:
    password -- the password to show.
    """
    if colors:
        print(f"{Fore.WHITE}Generated password: {Fore.MAGENTA + password + Fore.WHITE}")
    else:
        print(f"Generated password: {password}")
