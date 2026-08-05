from datetime import datetime

from sqlalchemy import ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.config.database import Base


class ProjectAccess(Base):
    __tablename__ = "projects_access"
    __table_args__ = (
        UniqueConstraint("project_id", "user_id", name="uq_project_user_access"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id", ondelete="CASCADE"), nullable=False
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    granted_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)

    project: Mapped["Project"] = relationship(back_populates="access_entries")
    user: Mapped["User"] = relationship(back_populates="project_access")