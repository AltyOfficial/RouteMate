import asyncio
import httpx

import pytest

from src.main import app


@pytest.mark.anyio
async def test_get_test():
    transport = httpx.ASGITransport(app=app)

    async with httpx.AsyncClient(transport=transport, base_url='http://127.0.0.1:8000') as client:
        resp = await client.get('/auth/test/')
        assert resp.status_code == 200
        assert resp.json() == {'test': 'ok'}
