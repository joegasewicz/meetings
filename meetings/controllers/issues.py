import logging

from sqlalchemy import select

from controllers import AbstractController
from exceptions import ControllerValueError
from models import (
    Model,
    IssueModel, StatusModel,
)
from utils.logger import log


class IssueController(AbstractController):
    def fetch_one(self, *, data: dict) -> Model | None:
        pass

    def fetch_all(self, *, data: dict) -> list[IssueModel]:
        project_id = data["project_id"]
        with self.get_session() as session:
            q = select(IssueModel)\
                .where(IssueModel.project_id == project_id)\
                .order_by(IssueModel.updated_date)
            return list(session.scalars(q).all())

    def create(self, *, data: dict) -> Model | None:
        try:
            name = data["name"]
            notes = data["notes"]
            deadline = data["deadline"]
            user_id = data["user_id"]
            project_id = data["project_id"]
            status_id = data["status_id"]
            with self.get_session() as session:
                issue = IssueModel()
                issue.name = name
                issue.notes = notes
                issue.deadline = deadline
                issue.user_id = user_id
                issue.project_id = project_id
                issue.status_id = status_id
                session.add(issue)
                session.commit()
                session.refresh(issue)
                return issue
        except ControllerValueError:
            log.error(f"Error saving new issue.", exc_info=True)

    def update(self) -> None:
        pass

    def remove(self) -> None:
        pass
