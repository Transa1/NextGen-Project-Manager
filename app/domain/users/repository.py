from abc import ABC, abstractmethod

from app.domain.users.entity import UserEntity


class UserRepository(ABC):
    @abstractmethod
    def get_by_email(self, email: str) -> UserEntity | None:
        ...

    @abstractmethod
    def get_by_id(self, user_id: int) -> UserEntity | None:
        ...

    @abstractmethod
    def create(self, email: str, password_hash: str, user_type_id: int) -> UserEntity:
        ...