web: gunicorn config.wsgi:application
worker: celery worker --app=blog.taskapp --loglevel=info
