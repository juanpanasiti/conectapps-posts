from pydantic import BaseModel


class Post(BaseModel):
    user_id: int
    id: int
    title: str
    body: str
