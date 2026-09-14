import sqlalchemy

from sqlalchemy import select

from meetings.controllers.base import AbstractController
from models import (
    Model,
    ProjectModel
)


class ProjectController(AbstractController):

    def fetch_one(self) -> Model | None:
        pass

    def fetch_all(self) -> list[Model]:
        with self.get_session() as session:
            return list(session.scalars(select(ProjectModel)).all())

    def create(self) -> None:
        pass

    def update(self) -> None:
        pass

    def remove(self) -> None:
        pass
