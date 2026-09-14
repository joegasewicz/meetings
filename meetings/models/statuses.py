from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey, func, TEXT
from sqlalchemy.orm import Mapped, mapped_column

from  meetings.models import Model


class StatusModel(Model):

    __tablename__ = "statuses"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
