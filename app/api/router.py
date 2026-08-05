from fastapi import APIRouter

from app.api.v1 import auth

api_router = APIRouter()

# POST /auth -> create user
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])

# POST /login -> login
api_router.add_api_route(
    "/login", auth.login, methods=["POST"], tags=["auth"], response_model=None
)