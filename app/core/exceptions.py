class DomainException(Exception):
    """Base exception"""


class UserAlreadyExistsError(DomainException):
    pass


class InvalidCredentialsError(DomainException):
    pass


class UserNotFoundError(DomainException):
    pass