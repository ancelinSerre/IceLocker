"""
Custom exception that may occur while generating a password
"""


class InvalidPasswordLengthError(Exception):
    """
    Raised when user tries to generate a password with less than 8 characters.
    """
    pass
