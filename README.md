# django-docker-compose-deploy
get start django docker example app

Clone the repo
   ```sh
   git clone https://github.com/shadhin-int/django-docker-compose-deploy
   ```
Create virtual environment and activate venv in project
```shell script
$ python -m venv venv
$ source venv/bin/activate
```

Install project dependencies and configure .env file
```
- Create *.env* file and copy *.env.example* and update all data
```
```shell script
$ pip install -r requirements.txt
```

commands:
```bash
docker-compose up
docker-compose run --rm app sh -c "python manage.py startapp foobar"
docker-compose run --rm app sh -c "python manage.py makemigrations foobar"
docker-compose run --rm app sh -c "python manage.py createsuperuser"
docker-comepose down -v
```
