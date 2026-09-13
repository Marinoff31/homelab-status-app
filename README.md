# homelab-status-app — CI/CD стартов проект

Малко Flask приложение, което съществува само за да мине през пълен
CI/CD цикъл: push → тестове → build на Docker image → deploy на
self-hosted runner в твоя home lab → scrape от Prometheus.

Пълното ръководство със стъпки е в артефакта "Пайплайн у дома",
изпратен заедно с тези файлове. Накратко:

1. `git init`, качи тези файлове в нов GitHub repo.
2. Инсталирай self-hosted runner на Ubuntu хоста (Settings → Actions
   → Runners → New self-hosted runner в repo-то).
3. Провери мрежата на твоя Grafana-Monitoring stack (`docker network
   ls`) и коригирай `docker-compose.deploy.yml`.
4. Push към `main` — GitHub Actions прави build + тестове на облачен
   runner, после deploy-ва през self-hosted runner-а у дома.
5. Добави `prometheus-scrape-snippet.yml` към `prometheus.yml` и
   направи `--force-recreate` на Prometheus, за да видиш приложението
   в Grafana.

## Локално, преди push

```bash
pip install -r requirements.txt
pytest -q
python app.py        # http://localhost:8088
```
