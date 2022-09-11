from server.config import constants
from server.database.blog_db import blog_db
from server.exceptions.db_exceptions import PopulatedDBError
from server.helpers.external_interface import PostsExternalInterface
from server.database.models.post_model import PostModel


class PostsService:
    def __init__(self):
        self.__posts_ei = None
        self.__db_conn = None

    @property
    def db_conn(self):
        if self.__db_conn is None:
            self.__db_conn = blog_db.conn
        return self.__db_conn

    @property
    def posts_ei(self):
        if self.__posts_ei is None:
            self.__posts_ei = PostsExternalInterface(constants.POSTS_URL_BASE)
        return self.__posts_ei

    def store_posts_seeds(self):
        result = blog_db.session.query(PostModel).count()
        if result > 0:
            raise PopulatedDBError('Posts DB is populated')
        seed = self.posts_ei.get(constants.POSTS_PATH)

        blog_db.session.add_all(
            [PostModel(**post) for post in seed]
        )
        blog_db.session.commit()
        return seed

    def get_posts(self, limit, offset):
        posts = blog_db.session.query(PostModel).limit(limit).offset(offset).all()
        return posts

    def get_post_by_id(self, id):
        posts = blog_db.session.query(PostModel).filter(
            PostModel.id == id).first()
        return posts
