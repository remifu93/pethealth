# PetHealth restfull server

## Setup

Install python

Install Postgresql Server and create database

create .env file following example .env.example

Create a virtual environment to install dependencies in and activate it:
```sh
$ python3 -m venv env
$ source env/bin/activate
```

Then install the dependencies:
```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py migrate
(env)$ python manage.py createsuperuser
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/admin`.