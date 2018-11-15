release: python manage.py migrate
web: gunicorn --pythonpath bank_detail_finder bank_detail_finder.wsgi:application
