# YaChef
Custom recipe service

## System description
A service for the application of custom recipes. 
Users can browse recipes, add their own recipes and perform various operations with them.

## To view the project locally, follow the steps below:

- clone the repository
- set up a virtual environment
```sh
pythom -m venv venv
```
- activate venv
- install project dependencies
```sh
pip install -r requirements.txt
```
- do migrations
```sh
python manage.py migrate
```
For statics, download [archive](https://code.s3.yandex.net/backend-developer/learning-materials/static.zip) and extract it into the directory ./posts/static/
- build static
```sh
python manage.py collectstatic
```
- create a superuser (optional)
```sh
python manage.py createsuperuser
```

## ToDo
I didn't set myself the task of accomplishing everything. 
I set myself the goal of showing my programming skin

- [x] Models with a minimum set of fields and links;
- [x] Templates
- [x] API
- [x] Tests post
- [x] Heroku
