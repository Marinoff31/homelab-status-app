# homelab-status-app — CI/CD стартов проект

Малко Flask приложение, което съществува само за да мине през пълен
CI/CD цикъл: push → тестове → build на Docker image → deploy на
self-hosted runner в твоя home lab → scrape от Prometheus.
