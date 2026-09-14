from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey, func, TEXT
from sqlalchemy.orm import Mapped, mapped_column

from  meetings.models import Model


class StandupNoteModel(Model):

    __tablename__ = "standup_notes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    note: Mapped[str] = mapped_column(TEXT, nullable=False)
    standup_date: Mapped[datetime] = mapped_column(DateTime(timezone=True))

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
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"), nullable=False)