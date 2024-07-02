docker compose stop && docker compose up --build

docker compose exec backend python manage.py collectstatic
docker compose exec backend cp -r /app/collected_static/. /backend_static/static/

docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py load_rickandmorty
