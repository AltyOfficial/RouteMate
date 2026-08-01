from src.application.dto.user import UserBaseDTO, UserCreateDTO
from src.infra.exceptions import (
    UserAlreadyExistsError,
)
from src.infra.security.password import PasswordHasher
from src.infra.uow import DatabaseUnitOfWork


class AuthService:
    def __init__(self, uow: DatabaseUnitOfWork):
        self.uow = uow

    async def register_user(self, payload: UserCreateDTO) -> UserBaseDTO:
        async with self.uow:
            existing_user = await self.uow.users.get_by_login(payload.login)
            if existing_user:
                raise UserAlreadyExistsError(
                    f"User with login '{payload.login}' already exists.",
                )

            password_hash = PasswordHasher.hash(payload.password)

            user_data = {
                "login": payload.login,
                "password_hash": password_hash,
                "is_active": True,
                "is_verified": False,
            }
            new_user = await self.uow.users.create(data=user_data)

            await self.uow.commit()

        return UserBaseDTO.model_validate(new_user)
