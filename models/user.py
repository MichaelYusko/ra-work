from enum import Enum

from sqlalchemy import Boolean, Column, DateTime, Integer, String

from db.compat import utcnow
from models import Base


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


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(254))
    password = Column(String(128))
    role = Column(Integer, default=UserRole.EMPLOYEE)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=utcnow())
    updated_at = Column(DateTime(timezone=True), onupdate=utcnow())
