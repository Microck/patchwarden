from fastapi.testclient import TestClient

from mod_sentinel.api.main import app


def test_health() -> None:
    client = TestClient(app)
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert data["service"] == "mod-sentinel"
    assert "version" in data
