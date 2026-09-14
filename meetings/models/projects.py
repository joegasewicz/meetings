from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey, func, TEXT
from sqlalchemy.orm import Mapped, mapped_column

from  meetings.models import Model


class ProjectModel(Model):

    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)

    created_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
    updated_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)