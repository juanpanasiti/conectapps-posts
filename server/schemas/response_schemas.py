from typing import List
from pydantic import BaseModel

from server.schemas.post_schema import Post


class SeedResponseData(BaseModel):
    created: bool
    seeds: int


class SeedResponse(BaseModel):
    response_data: SeedResponseData


class PostResponse(BaseModel):
    response_data: Post


class PaginatedPostResponse(BaseModel):
    response_data: List[Post]
    items: int
    total: int
