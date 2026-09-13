"""
homelab-status-app
Малко Flask приложение за практика на CI/CD пайплайн.
Излага /health (за deploy проверка) и /metrics (Prometheus format,
за да се включи като scrape target в съществуващия ти stack).
"""

import time
from flask import Flask, Response, jsonify

app = Flask(__name__)
START_TIME = time.time()
REQUEST_COUNT = 0


@app.route("/")
def index():
    global REQUEST_COUNT
    REQUEST_COUNT += 1
    return jsonify(service="homelab-status-app", status="ok")


@app.route("/health")
def health():
    """Ползва се от CD стъпката, за да провери дали deploy-ът е успешен."""
    return jsonify(status="healthy"), 200


@app.route("/metrics")
def metrics():
    """Prometheus text-format метрики — добави job в prometheus.yml."""
    uptime = time.time() - START_TIME
    body = (
        "# HELP app_uptime_seconds Time since the app started\n"
        "# TYPE app_uptime_seconds counter\n"
        f"app_uptime_seconds {uptime:.2f}\n"
        "# HELP app_requests_total Total requests to /\n"
        "# TYPE app_requests_total counter\n"
        f"app_requests_total {REQUEST_COUNT}\n"
    )
    return Response(body, mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8088)
