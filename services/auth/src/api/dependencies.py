from fastapi import Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.services.auth import AuthService
from src.infra.database.sessions import get_async_session
from src.infra.uow import DatabaseUnitOfWork


def get_auth_service(
    db_session: AsyncSession = Depends(get_async_session),
) -> AuthService:
    uow = DatabaseUnitOfWork(db_session)
    return AuthService(uow=uow)


def get_client_info(request: Request) -> tuple[str, str]:
    device_info = request.headers.get('User-Agent')
    ip_address = request.client.host
    return device_info, ip_address
