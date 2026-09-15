from controllers import AbstractController
from models import Model


class IssueController(AbstractController):
    def fetch_one(self, *, data: dict) -> Model | None:
        pass

    def fetch_all(self) -> list[Model]:
        pass

    def create(self, *, data: dict) -> Model | None:
        pass

    def update(self) -> None:
        pass

    def remove(self) -> None:
        pass
