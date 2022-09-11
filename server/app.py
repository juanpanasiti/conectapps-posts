from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from datetime import datetime

from server.api.v1 import router_v1
# from server.config.log import TimedRoute
from server.database import blog_db

app = FastAPI(
    title='PostsConectApps',
    version='1.0.0',
    description='API for the technical challenge for ConectApps.',
    debug=False
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Logging
logging.basicConfig(
    level=logging.INFO,
    filemode='a',
    filename='./logs/{}'.format(datetime.now().strftime('%Y%m%d_api.log')),
)

# Routers
# app.router.route_class = TimedRoute

app.router.prefix = '/api'
app.include_router(router_v1)

# DB
blog_db.generate_tables()
