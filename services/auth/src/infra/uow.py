from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.repositories.user_sqla import UserRepository


class DatabaseUnitOfWork:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def __aenter__(self):
        self.users = UserRepository(session=self.session)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()
        pass

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        if self.session.is_active:
            await self.session.rollback()
