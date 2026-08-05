from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserEntity:
    id: int | None
    user_type_id: int
    email: str
    password_hash: str
    created_at: datetime | None = None