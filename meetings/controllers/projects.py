import sqlalchemy

from sqlalchemy import select

from meetings.controllers.base import AbstractController
from models import (
    Model,
    ProjectModel
)
from meetings.exceptions import ControllerValueError
from utils.logger import log


class ProjectController(AbstractController):

    def fetch_one(self, *, data: dict) -> ProjectModel | None:
        try:
            project_id = data["project_id"]
            with self.get_session() as session:
                return session.execute(
                    select(ProjectModel).where(ProjectModel.id==project_id)
                ).scalar_one_or_none()
        except ControllerValueError:
            log.error(f"Missing 'project_id' key.")
            return None

    def fetch_all(self) -> list[ProjectModel]:
        with self.get_session() as session:
            return list(session.scalars(select(ProjectModel)).all())

    def create(self, *, data: dict) -> ProjectModel | None:
        try:
            name = data["name"]
            user_id = data["user_id"]
            with self.get_session() as session:
                project = ProjectModel()
                project.name = name
                project.user_id = user_id
                session.add(project)
                session.commit()
                session.refresh(project)
                return project
        except ControllerValueError:
            log.error(
                f"New Project model is missing key value(s).",
                exc_info=True,
            )

    def update(self) -> None:
        pass

    def remove(self) -> None:
        pass
