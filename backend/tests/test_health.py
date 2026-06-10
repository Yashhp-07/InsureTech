from httpx import AsyncClient, ASGITransport
import pytest

from app.main import app


@pytest.fixture
def client():
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")


@pytest.mark.asyncio
async def test_root(client):
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "InsureTech API is running"}


@pytest.mark.asyncio
async def test_health(client):
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
