from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from exceptions import ControllerValueError
from meetings.controllers.base import AbstractController
from models import Model, StatusModel
from utils.logger import log


class StatusController(AbstractController):

    def fetch_one(self, *, data: dict) -> Model | None:
        try:
            name = data["name"]
            with self.get_session() as session:
                q = select(StatusModel).where(StatusModel.name == name)
                status = session.scalar(q)
                return status
        except ControllerValueError:
            log.error(f"Error fetching status")

    def fetch_all(self) -> list[StatusModel]:
        with self.get_session() as session:
            return list(session.scalars(select(StatusModel)).all())

    def create(self, *, data: dict) -> list[StatusModel] | None:
        try:
            names = data["names"]
            with self.get_session() as session:
                statuses = []
                for name in names:
                    status = StatusModel(name=name)
                    session.add(status)
                    session.commit()
                    session.refresh(status)
                    statuses.append(status)
            return statuses
        except ControllerValueError:
           log.error("Error creating new status", exc_info=True)
        except IntegrityError:
            pass

    def update(self) -> None:
        pass

    def remove(self) -> None:
        pass
