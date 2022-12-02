# todolist
a todolist with django

## End Points
![7be481be854c4c6b2575aaaceac2c2d](https://user-images.githubusercontent.com/17155788/205271532-7101a5be-3ee8-4c4c-aa42-9273d3d435bd.png)

## Documentation
All the API docs are available in **http://0.0.0.0:8000/docs/** builded with [**OpenAPI schema**](https://www.django-rest-framework.org/topics/documenting-your-api/)

# Installation process 

## Install the system dependencies
`pip install -r ./requirementstxt`

## Run the command to generate the database
`python manage.py migrate`

## Generate super user
`python manage.py createsuperuser`

## Run the server
`python manage.py runserver` the application will be running on port 8000 **http://0.0.0.0:8000/**

## Run the test
`python manage.py test`
