python books/manage.py makemigrations
python books/manage.py migrate --database master
python books/manage.py populate_db
python books/manage.py runserver 0.0.0.0:8000
