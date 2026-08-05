from datetime import datetime

from sqlalchemy import String, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.config.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_type_id: Mapped[int] = mapped_column(ForeignKey("user_types.id"), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)


    user_type: Mapped["UserType"] = relationship(back_populates="users")

    projects_created: Mapped[list["Project"]] = relationship(
        back_populates="created_by_user",
        foreign_keys="Project.created_by",
    )
    projects_updated: Mapped[list["Project"]] = relationship(
        back_populates="updated_by_user",
        foreign_keys="Project.updated_by",
    )
    documents_uploaded: Mapped[list["Document"]] = relationship(back_populates="uploaded_by_user")
    project_access: Mapped[list["ProjectAccess"]] = relationship(back_populates="user")