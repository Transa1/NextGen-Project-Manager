from sqlalchemy.orm import Session

from app.domain.users.entity import UserEntity
from app.domain.users.repository import UserRepository
from app.infrastructure.persistence.orm.models.user import User


class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, db: Session):
        self.db = db

    def _to_entity(self, user: User) -> UserEntity:
        return UserEntity(
            id=user.id,
            user_type_id=user.user_type_id,
            email=user.email,
            password_hash=user.password_hash,
            created_at=user.created_at,
        )

    def get_by_email(self, email: str) -> UserEntity | None:
        user = self.db.query(User).filter(User.email == email).first()
        return self._to_entity(user) if user else None

    def get_by_id(self, user_id: int) -> UserEntity | None:
        user = self.db.query(User).filter(User.id == user_id).first()
        return self._to_entity(user) if user else None

    def create(self, email: str, password_hash: str, user_type_id: int) -> UserEntity:
        user = User(email=email, password_hash=password_hash, user_type_id=user_type_id)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return self._to_entity(user)