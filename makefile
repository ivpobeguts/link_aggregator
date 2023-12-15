migrate:
	poetry run python django_app/manage.py migrate

run:
	poetry run python django_app/manage.py runserver

test:
	poetry run python django_app/manage.py test

flake8:
	poetry run flake8 django_app --max-line-length 100

isort:
	poetry run isort django_app

