build:
	docker compose up -d --build

up:
	docker compose up

show_logs:
	docker compose logs -f

down:
	docker compose down

makemigrations:
	docker compose exec web python manage.py makemigrations

migrate:
	docker compose exec web python manage.py migrate

restart:
	sudo systemctl restart gunicorn

createsuperuser:
	docker compose exec web python manage.py createsuperuser
