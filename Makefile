migrate:
	python manage.py makemigrations & python manage.py migrate

run:
	python manage.py runserver

createsuperuser:
	python manage.py createsuperuser