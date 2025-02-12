from typing import NamedTuple

# Tuples


class Auth(NamedTuple):
    """Tuple for an authentication object

    Attributes
        email: The email to authenticate with.
        password: The password to authenticate with.
    """

    email: str
    password: str


# Exceptions / Errors


class CarrierError(Exception):
    """
    Exception raised for an invalid carrier

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class EmailError(Exception):
    """
    Exception raised for invalid email.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class PasswordError(Exception):
    """
    Exception raised for invalid email.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
