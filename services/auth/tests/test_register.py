from httpx import AsyncClient


async def test_register(client: AsyncClient):
    body = {
        'login': 'admin',
        'password': 'admin',
    }
    resp = await client.post('/auth/register/', json=body)
    assert resp.status_code == 201
