from sqlalchemy import create_engine, orm

from server.exceptions.db_exceptions import ConnectionDBError

from server.config.db import Base, connection_url


class BlogDB:
    def __init__(self):
        self.__engine = None
        self.__session = None

    @property
    def engine(self):
        if self.__engine is None:
            conn_url = connection_url
            self.__engine = create_engine(conn_url)
        return self.__engine

    @property
    def session(self):
        if self.__session is None:
            Session = orm.sessionmaker(bind=self.engine)
            self.__session = Session()
        return self.__session

    def generate_tables(self):
        try:
            Base.metadata.create_all(self.engine)
        except Exception as ex:
            raise ConnectionDBError(str(ex))


blog_db = BlogDB()
