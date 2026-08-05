from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import get_auth_service
from app.application.auth.service import AuthService
from app.core.exceptions import UserAlreadyExistsError, InvalidCredentialsError
from app.domain.auth.schemas import RegisterRequest, LoginRequest, TokenResponse

router = APIRouter()


@router.post("", status_code=status.HTTP_201_CREATED)
def register_user(
    data: RegisterRequest,
    auth_service: AuthService = Depends(get_auth_service),
):
    try:
        auth_service.register(data)
    except UserAlreadyExistsError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    return {"message": "User created successfully"}


@router.post("/login", response_model=TokenResponse)
def login(
    data: LoginRequest,
    auth_service: AuthService = Depends(get_auth_service),
):
    try:
        return auth_service.login(data)
    except InvalidCredentialsError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))