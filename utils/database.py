from functools import cache

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Engine

from config import Config
from utils.logger import log


class Database:

    engine: Engine

    def __init__(self, *, config: Config):
        self.config = config

    @cache
    def get_engine(self, conn_str: str) -> Engine:
        """
        Let the engine raise if the connection string is incorrect
        :param conn_str:
        :return:
        """
        log.info(f"Creating new SQLALchemy Engine")
        engine = create_engine(conn_str)
        return engine

    def get_db_conn(self) -> str:
        """
        Get the db connection string
        :return:
        """
        url = f"sqlite:///{self.config.SQLITE_DATABASE_NAME}"
        return url

    def get_session(self) -> Session:
        self.conn_str = self.get_db_conn()
        self.engine = self.get_engine(conn_str=self.conn_str)
        self.db_session_factory = sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
        )
        return self.db_session_factory()
