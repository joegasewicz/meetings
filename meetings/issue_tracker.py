from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

from config import Config
from utils.database import Database

from utils.logger import log
from meetings.models import (
    Model,
    tables,
)


class IssueTracker:

    # If a user has a paid subscription, then use remote Postgres
    has_subscription: bool
    db_type: str = "sqlite"
    database: Database
    db_session_factory: sessionmaker[Session]

    def __init__(self, *, config: Config):
        self.config = config
        self.has_subscription = self._user_has_subscription()
        if self.has_subscription:
            """TODO use remote Postgres here..."""
        else:
            self.database = Database(config=config)
            conn_str = self.database.get_db_conn()
            engine = self.database.get_engine(conn_str=conn_str)
            self.db_session_factory = sessionmaker(
                bind=engine,
                autoflush=False,
                autocommit=False,
            )
            Model.metadata.create_all(engine, tables=tables)
            log.info("Creating local tables")
            for table in Model.metadata.sorted_tables:
                log.info(f"\t- {table}")


    def _user_has_subscription(self) -> bool:
        """
        The MVP only uses a local sqlite db.
        :return:
        """
        return False