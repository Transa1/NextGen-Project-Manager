from app.config.security import hash_password, verify_password, create_access_token
from app.core.exceptions import UserAlreadyExistsError, InvalidCredentialsError
from app.domain.auth.schemas import RegisterRequest, LoginRequest, TokenResponse
from app.domain.users.repository import UserRepository

DEFAULT_USER_TYPE_ID = 2


class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register(self, data: RegisterRequest) -> None:
        existing_user = self.user_repository.get_by_email(data.email)
        if existing_user:
            raise UserAlreadyExistsError(f"User with email {data.email} already exists")

        password_hash = hash_password(data.password)
        self.user_repository.create(
            email=data.email,
            password_hash=password_hash,
            user_type_id=DEFAULT_USER_TYPE_ID,
        )

    def login(self, data: LoginRequest) -> TokenResponse:
        user = self.user_repository.get_by_email(data.email)
        if not user or not verify_password(data.password, user.password_hash):
            raise InvalidCredentialsError("Invalid email or password")

        token = create_access_token(subject=str(user.id))
        return TokenResponse(access_token=token)