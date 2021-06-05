# django-docker-compose-deploy
get start django docker example app

commands:
```bash
docker-compose up
docker-compose run --rm app sh -c "python manage.py startapp foobar"
docker-compose run --rm app sh -c "python manage.py makemigrations foobar"
docker-compose run --rm app sh -c "python manage.py createsuperuser"
docker-comepose down -v
```
