migrate:
	python manage.py makemigrations & python manage.py migrate

run:
	python manage.py runserver

createsuperuser:
	python manage.py createsuperuser

install:
	pip install -r reqs\dev.txt

freeze:
	pip freeze > reqs\dev.txt