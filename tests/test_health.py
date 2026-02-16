from fastapi.testclient import TestClient

from jarspect.api.main import app


def test_health() -> None:
    client = TestClient(app)
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert data["service"] == "jarspect"
    assert "version" in data
