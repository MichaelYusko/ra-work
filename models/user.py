from enum import Enum


class UserRole(Enum):
    EMPLOYEE = 1
    MANAGER = 2


class AnonymousUser:
    id = None
    ERROR = 'System doesn\'t provide a DB representation for AnonymousUser.'

    def __str__(self):
        return 'AnonymousUser'

    def is_authenticated(self):
        return False

    def create_user(self, first_name, last_name, email, role):
        raise NotImplementedError(self.ERROR)

    def check_password(self, password):
        return NotImplementedError(self.ERROR)

    def set_password(self, password):
        raise NotImplementedError(self.ERROR)
