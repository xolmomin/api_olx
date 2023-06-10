migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

admin:
	python3 manage.py createsuperuser --username=admin --email=admin@mail.ru --noinput


export_req:
	poetry export --without-hashes --format=requirements.txt > requirements.txt

check:
	flake8 .
	isort .

