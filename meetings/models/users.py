from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey, func, TEXT
from sqlalchemy.orm import Mapped, mapped_column

from  meetings.models import Model


class UserModel(Model):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=True)
    password: Mapped[str] = mapped_column(String(120), nullable=True)
    full_name: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)

    created_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
    updated_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
