from meetings.controllers.base import AbstractController
from models import Model


class ProjectController(AbstractController):

    def fetch_one(self) -> type[Model]:
        pass

    def fetch_all(self) -> type[list[Model]]:
        pass

    def create(self) -> None:
        pass

    def update(self) -> None:
        pass

    def remove(self) -> None:
        pass
