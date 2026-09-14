from abc import ABC, abstractmethod

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

from meetings.models import Model
from utils.database import Database


class AbstractController(ABC):

    def __init__(self, database: Database):
        self.database = database

    def get_session(self) -> Session:
        """
        Returns a SQLAlchemy Session
        :return:
        """
        return self.database.get_session()

    @abstractmethod
    def fetch_one(self) -> Model | None: ...

    @abstractmethod
    def fetch_all(self) -> list[Model]: ...

    @abstractmethod
    def create(self) -> None: ...

    @abstractmethod
    def update(self) -> None: ...

    @abstractmethod
    def remove(self) -> None: ...
