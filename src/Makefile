PYTHON := $(CURDIR)/../venv/Scripts/python.exe
PORT := 8000

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

runserver:
	$(PYTHON) manage.py runserver $(PORT)

createsuperuser:
	python manage.py createsuperuser

install:
	$(PYTHON) -m pip install -r requirements.txt

freeze:
	$(PYTHON) -m pip freeze > requirements.txt