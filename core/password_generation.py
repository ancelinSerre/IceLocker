"""
Set of functions used to generate a random password following some 
user specified rules like sets of characters to use, or password length
"""
import logging
import math
import random
import re
from string import ascii_lowercase, ascii_uppercase, punctuation, digits
from typing import Dict, Optional, Tuple

from core import InvalidPasswordLengthError

CHAR_OPTIONS = {
    "lowercase": ascii_lowercase,
    "uppercase": ascii_uppercase,
    "specials": punctuation,
    "digits": digits
}


def build_lexicon(character_options: Optional[Dict] = None) -> str:
    """
    Build a character lexicon that is compliant with user specified options.
    Return the lexicon as a string.

    Keyword arguments:
    character_options -- password options (length, user lowercase chars, etc.)
    """
    if character_options:
        return "".join([CHAR_OPTIONS[o] for o in CHAR_OPTIONS if character_options.get(o)])

    # Use default character options
    return ascii_lowercase + ascii_uppercase + punctuation + digits


def build_verification_regex(length: int, char_options: Dict[str, bool]) -> str:
    """
    Build a regular expression string that will allow
    to verify if a given password is compliant with the specified options.

    Arguments:
    length -- password length
    char_options -- password character options (use lowercase chars, etc.)
    """
    # Set min length
    password_check_pattern = f"^(.{{0,{length - 1}}}"
    for option in (o for o in char_options if char_options[o]):
        if option == "lowercase":
            password_check_pattern += "|[^a-z]*"  # No lowercase
        elif option == "uppercase":
            password_check_pattern += "|[^A-Z]*"  # No uppercase
        elif option == "specials":
            password_check_pattern += "|[a-zA-Z0-9]*"  # No special char
        elif option == "digits":
            password_check_pattern += "|[^0-9]*"  # No digit

    password_check_pattern += ")$"
    return password_check_pattern


def generate_password(length: int, char_options: Dict[str, bool], lexicon: str) -> str:
    """
    Generate a random password that is compliant with user specified options.
    Return the password as a string.

    Arguments:
    length -- password length
    char_options -- password character options (use lowercase chars, etc.)
    lexicon -- character lexicon that will be used to generate the password
    """
    if length < 8:
        raise InvalidPasswordLengthError(
            "You must specify a password length >= 8")

    password: str = ""

    if not char_options:
        logging.debug("No character options found for password, use default")
        char_options = {
            "lowercase": True,
            "uppercase": True,
            "specials": True,
            "digits": True
        }

    verification_regex: str = build_verification_regex(length, char_options)
    verification_regex_compiled: re.Pattern = re.compile(verification_regex)

    while True:
        for _ in range(length):
            password += random.choice(lexicon)

        # Check if candidate password is compliant
        match_res = verification_regex_compiled.match(password)
        if match_res is not None:
            logging.debug("Invalid password, recreating... %s", password)
            password = ""
        else:
            # Password is compliant, break the loop
            break

    return password


def compute_password_strength(password: str, lexicon: str) -> Tuple[str, float]:
    """
    Compute password strenght using its entropy (in bits).
    Returns a string representing the password strength and its entropy in bits.

    Arguments:
    password -- password string
    lexicon -- character lexicon used to generate password
    """
    entropy: float = len(password) * math.log2(len(lexicon))
    if entropy < 28:
        return ("Very weak", entropy)
    elif entropy < 35:
        return ("Weak", entropy)
    elif entropy < 59:
        return ("Reasonable", entropy)
    elif entropy < 127:
        return ("Strong", entropy)
    else:
        return ("Very strong", entropy)
