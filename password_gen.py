"""
Password generator CLI
"""
import argparse
import random
import logging
from datetime import datetime
from typing import Dict, Tuple

from colorama import Fore

from core import (
    build_lexicon, compute_password_strength, generate_password, InvalidPasswordLengthError 
)
from cli import (
    parse_arguments, prepare_password_options, show_password, show_password_strength
)

if __name__ == "__main__":

    logging.basicConfig(
        level=logging.DEBUG,
        format=("[%(asctime)s] %(levelname)s | %(message)s"),
        handlers=[logging.FileHandler("password_gen.log")])

    args: argparse.Namespace = parse_arguments()
    length: int = 0
    char_options: Dict[str, bool] = {}
    length, char_options = prepare_password_options(args)

    # Set seed for the random character generator
    # using float representation of the current datetime
    random.seed(datetime.now().timestamp())

    lexicon: str = build_lexicon(char_options)
    try:
        password: str = generate_password(args.length, char_options, lexicon)
    except InvalidPasswordLengthError:
        logging.exception("Invalid password length: ")
        print(f"{Fore.RED}You must use a password length >= 8 characters.{Fore.WHITE}")
        exit(-1)
    except Exception:
        logging.exception("Unexpected exception: ")
        print(
            f"{Fore.RED}Something went wrong! Check logs for more informations.{Fore.WHITE}")
        exit(-1)
    else:
        password_strength: Tuple[str, float] = compute_password_strength(password, lexicon)
        logging.info("Password generated")
        logging.info(
            "Strength: %s ; Entropy: %0.2f bits",
            password_strength[0], password_strength[1]
        )
        show_password(password, colors=False)
        show_password_strength(*password_strength, colors=True)
