from fastapi import APIRouter

from .posts_routes import router as posts_router

router_v1 = APIRouter(prefix='/v1')

router_v1.include_router(posts_router, tags=['Posts', 'v1'])
