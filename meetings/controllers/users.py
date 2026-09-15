from sqlalchemy import select

from meetings.controllers.base import AbstractController
from models import UserModel


class UserController(AbstractController):

    def fetch_one(self) -> UserModel | None:
        pass

    def fetch_all(self) -> list[UserModel]:
        pass

    def create(self, *, data: dict) -> UserModel | None:
        with self.get_session() as session:

            existing_user = session.execute(
                select(UserModel).where(UserModel.email=="default@email.com")
            ).scalar_one_or_none()

            if existing_user:
                return existing_user

            user = UserModel(
                email=data.get("email", "default@email.com"),
                password=data.get("password", "default"),
                full_name=data.get("full_name", "user #1"),
            )
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def update(self) -> None:
        pass

    def remove(self) -> None:
        pass