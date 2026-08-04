from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class UserRegisterSchema(BaseModel):
    login: str
    password: str


class UserResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    login: str
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime
