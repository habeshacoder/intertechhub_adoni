# InternTechHub Django Project
///////////////////////////////////////////////

# stage_3

# How to run this project locally?

- clone this project

- install the requirements.tx file

> pip install -r requirements.txt

- install the requirements.dev.txt (optional)

> pip install -r requirements.dev.txt

- start the server

> python manage.py runserver

# How to test this project in production

- navigate to this url:

  https://intertechhub-adoni.onrender.com

- Use the API Documentation (Swagger UI) to test this project:

  https://intertechhub-adoni.onrender.com/api/docs/

///////////////////////////////////////////////

# stage_2

# How to run this project locally?

- clone this project

- install the requirements.tx file

> pip install -r requirements.txt

- install the requirements.dev.txt (optional)

> pip install -r requirements.dev.txt

- start the server

> python manage.py runserver

# How to test this project in production

- navigate to this url:

  https://intertechhub-adoni.onrender.com

- Use the API Documentation (Swagger UI) to test this project:

  https://intertechhub-adoni.onrender.com/api/docs/

  //////////////////////////////////////////////////////

# stage_1

- this is a django application responds an httpresponse based on the request. It responses a predefined a person's name, hobbies and dreams based on the the http request. This app also handles incase there is no resource for the incoming request

## Table of Contents

- [Features](#features)

- [Prerequisites](#prerequisites)

- [Configuration](#configuration)

## Features

- Responds with a welcome message on the '/' root route.
- Returns a person's name at the '/name' route.
- Returns a list of hobbies at the '/hobby' route.
- Returns a personal dream at the '/dream' route.
- Handles undefined routes with a 404 Not Found response.

### Prerequisites

- Python 3.x
- Django 5.x

### configuration

- Create a folder
- Then create a vertual environment
- Activate the the created vertual environment
- Then install django
- git clone https://github.com/habeshacoder/intertechhub_adoni.git
- cd intertechhub_adoni
- python manage.py runserver (if you want to work on local machine. the default port is 8000)

Creating a vertual environment is optional. But to make clean development for python projects it saves your life!
