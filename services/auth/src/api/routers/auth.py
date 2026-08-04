import logging

from fastapi import APIRouter, Depends, HTTPException, status

from src.api.dependencies import get_auth_service
from src.api.schemas.auth import (
    UserRegisterSchema,
    UserResponseSchema,
)
from src.application.services.auth import AuthService

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)


@router.get(
    '/test/',
)
async def test():
    return {'test': 'ok'}




@router.post(
    '/register/',
    description='Register new User',
    status_code=status.HTTP_201_CREATED,
)
async def register_user(
    payload: UserRegisterSchema,
    service: AuthService = Depends(get_auth_service),
) -> UserResponseSchema:

    try:
        user = await service.register_user(payload=payload)
    except Exception as exc:
        logging.error(f"Error registering user: {exc}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="server error",
        ) from exc

    return UserResponseSchema.model_validate(user)
