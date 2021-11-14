release: ./release-tasks.sh
web: gunicorn pydjango_ci_integration.wsgi --log-file -
worker: memcached