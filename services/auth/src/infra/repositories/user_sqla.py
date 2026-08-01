from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.database.models import UserModel


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: dict) -> UserModel:
        user = UserModel(**data)
        self.session.add(user)
        await self.session.flush()

        return user

    async def get_by_login(self, login: str) -> UserModel | None:
        stmt = select(UserModel).where(UserModel.login == login)
        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()
