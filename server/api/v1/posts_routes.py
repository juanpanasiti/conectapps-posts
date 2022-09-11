import logging
from fastapi import APIRouter, HTTPException, Path, Query
from server.config.log import TimedRoute
from server.exceptions.db_exceptions import PopulatedDBError

from server.schemas.response_schemas import (
    PaginatedPostResponse, PostResponse, SeedResponse, SeedResponseData
)
from server.services.posts_services import PostsService

logger = logging.getLogger()

router = APIRouter(prefix='/posts', route_class=TimedRoute)
posts_service = PostsService()


# Charge the DB with the seed of posts
@router.post(
    '/seed',
    response_model=SeedResponse,
    status_code=201,
    name='Seed the table post',
    description='Populate the table \'post\' with some records from an external api'
)
async def charge_seed_post():
    '''
    Long description
    '''
    try:
        posts_seed = posts_service.store_posts_seeds()
    except PopulatedDBError as pdb_error:
        raise HTTPException(
            status_code=400,
            detail="The posts table that you are trying to seed is non empty",
            headers={'server-error': str(pdb_error)},
        )
    return SeedResponse(
        response_data=SeedResponseData(
            created=True,
            seeds=len(posts_seed)
        )
    )


@router.get(
    '',
    response_model=PaginatedPostResponse,
    name='Get posts paginated',
    description='Get a list of Post objects (JSON) paginated (with params limit y skip)',
)
async def get_paginated(
    limit: int = Query(ge=1, le=100, default=10),
    skip: int = Query(ge=0, default=0)
):
    posts = posts_service.get_posts(limit, skip)
    return PaginatedPostResponse(
        response_data=[post.to_dict() for post in posts],
        items=len(posts),
        total=0
    )


@router.get(
    '/{id}',
    response_model=PostResponse,
    name='Get a post by ID',
    description='',
)
async def get_by_id(id: int = Path(gt=0)):
    post = posts_service.get_post_by_id(id)

    if post is None:
        raise HTTPException(
            status_code=404,
            detail=f'The post with id #{id} was not found.'
        )
    return PostResponse(response_data=post.to_dict())
