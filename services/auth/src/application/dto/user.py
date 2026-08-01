from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class UserBaseDTO(BaseModel):
    id: UUID
    login: str
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UserCreateDTO(BaseModel):
    login: str
    password: str
