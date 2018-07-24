release: python manage.py migrate --no-input --settings=MIT_OCW_Server.production
web: gunicorn MIT_OCW_Server.wsgi --log-file -