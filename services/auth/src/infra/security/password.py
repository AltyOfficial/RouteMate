import asyncio

import bcrypt


class PasswordHasher:
    @staticmethod
    def hash(password: str) -> str:
        pwd_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password=pwd_bytes, salt=salt)

        return password_hash.decode('utf-8')

    @staticmethod
    async def verify(password: str, hashed_password: str) -> bool:

        password_byte_enc = password.encode('utf-8')
        hashed_password_enc = hashed_password.encode('utf-8')

        is_valid = await asyncio.to_thread(
            bcrypt.checkpw,
            password_byte_enc,
            hashed_password_enc,
        )

        return is_valid
