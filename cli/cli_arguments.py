"""
Set of functions used to read CLI arguments
"""
import argparse
from typing import Dict, Iterator, Tuple


def parse_arguments() -> argparse.Namespace:
    """
    CLI arguments parser.
    All password generation arguments are defined here.
    Return the argument namespace.
    """
    parser = argparse.ArgumentParser(description="Simple password generator")
    parser.add_argument("-l", "--length", type=int, default=8,
                        help="Password length")
    parser.add_argument("-a", "--all", action="store_true",
                        help="Use lower/upper case characters, digits and specials")
    parser.add_argument("-lc", "--lowercase", action="store_true",
                        help="Use lower case characters")
    parser.add_argument("-uc", "--uppercase", action="store_true",
                        help="Use upper case characters")
    parser.add_argument("-s", "--specials", action="store_true",
                        help="Use special characters")
    parser.add_argument("-d", "--digits", action="store_true",
                        help="Use digits")

    return parser.parse_args()


def prepare_password_options(args: argparse.Namespace) -> Tuple[int, Dict[str, bool]]:
    """
    Function used to prepare the password generation options (length, character sets).
    Return a Tuple containing the length and the character options.

    Arguments:
    args -- argument namespace collected by the program.
    """
    char_options: Iterator[bool] = (
        args.lowercase, args.uppercase, args.specials, args.digits)

    if args.all or all((not opt for opt in char_options)):
        char_options = {
            "lowercase": True,
            "uppercase": True,
            "specials": True,
            "digits": True
        }
    else:
        char_options = {
            "lowercase": args.lowercase,
            "uppercase": args.uppercase,
            "specials": args.specials,
            "digits": args.digits
        }

    return (args.length, char_options)
