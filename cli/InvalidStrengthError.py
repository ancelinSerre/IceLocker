"""
Custom exception that may occur while showing the password strength
"""


class InvalidStrengthError(Exception):
    """
    Raised when an invalid strength (unknown one) is provided to function colorize_strength.
    """
    pass
