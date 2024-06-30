from fastapi import FastAPI, Depends, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware
from routers import all_routers

# print(datetime.now())

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]


app = FastAPI(
    title="Backend API",
    debug=True,
    description="API endpoints for FYP backend (..))",
    version="1.0.0",
    middleware=middleware,
    openapi_url="/v1/openapi.json",
    docs_url="/v1/docs",
    redoc_url="/v1/redoc",
)
app.include_router(all_routers.login_router)
app.include_router(all_routers.router)
app.include_router(all_routers.router3)
app.include_router(all_routers.router4)
app.include_router(all_routers.common)


app.include_router(all_routers.router2)
app.include_router(all_routers.router5)
