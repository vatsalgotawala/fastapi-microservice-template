import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from myservice.config import config
from myservice.main import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_healthcheck():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(f"{config.openapi_prefix}/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "down"}


def test_versioninfo():
    response = client.get(f"{config.openapi_prefix}/versioninfo")
    json_response = response.json()
    assert response.status_code == 200
    assert json_response.get("packageName") == config.app_name
    assert "versionInfo" in json_response.keys()


def test_versioninfo_exception():
    response = client.get(f"{config.openapi_prefix}/versioninfo?packageName=madeup")
    assert response.status_code == 404
    assert response.json() == {
        "app_exception": "PackageNotFoundException",
        "content": {"message": "Package not found", "package_name": "madeup"},
    }
