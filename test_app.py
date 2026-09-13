"""
Много прости тестове — целта им е да дадат на CI стъпката нещо
реално за проверка, преди да се стигне до build/deploy.
"""

from app import app


def test_health_returns_200():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "healthy"


def test_metrics_exposes_prometheus_format():
    client = app.test_client()
    resp = client.get("/metrics")
    assert resp.status_code == 200
    assert b"app_uptime_seconds" in resp.data
    assert b"app_requests_total" in resp.data


def test_index_counts_requests():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.get_json()["service"] == "homelab-status-app"
