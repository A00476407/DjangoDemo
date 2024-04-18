# Django Assignment
This is a Django application which is connected to a remote MySQL database and provides REST API to access the data.

# Create virtual environment (if required)
1. Run `py -m venv venv`

# Run virtual environment
1. Navigate to the `venv/Scripts/` directory
2. Run `activate.bat`

# Install Django (if required)
1. After activating the environment, run `py -m pip install`

# Database Setting 
1. Naviagte to the `django_demo/django_demo/settings.py` directory
2. Update database connection setting in line 78-87
3. Naviagte to the `django_demo/` directory
4. python manage.py makemigrations
5. python manage.py migrate
> [!NOTE]
> If you are not using your own database, you may skip the database setting.

# Build and Run the application
1. Navigate to the `django_demo/` directory
2. Run `python manage.py runserver`

# Accessing the REST API
## GET API (Function Based)
- Get a list of available hotels room
- URL: localhost:8000/app/roomlist
![alt text](https://github.com/A00476407/DjangoDemo/blob/main/Screenshots/GET.png?raw=true)

## POST API (Function Based)
- Add a room entry with JSON request body
- URL: localhost:8000/app/roomlist
```JSON
{
  "price": 400,
  "type_id": 1
}
```
![alt text](https://github.com/A00476407/DjangoDemo/blob/main/Screenshots/POST.png?raw=true)
![alt text](https://github.com/A00476407/DjangoDemo/blob/main/Screenshots/POST_result.png?raw=true)
![alt text](https://github.com/A00476407/DjangoDemo/blob/main/Screenshots/POST_result2.png?raw=true)

## GET API (Class Based)
- Get a list of available hotels room
- URL: localhost:8000/app/classrooms
![alt text](https://github.com/A00476407/DjangoDemo/blob/main/Screenshots/class_GET.png?raw=true)

## POST API (Class Based)
- Add a room entry with JSON request body
- URL: localhost:8000/app/classrooms
```JSON
{
  "price": 500,
  "type_id": 2
}
```
![alt text](https://github.com/A00476407/DjangoDemo/blob/main/Screenshots/class_POST.png?raw=true)
![alt text](https://github.com/A00476407/DjangoDemo/blob/main/Screenshots/class_POST_result.png?raw=true)
![alt text](https://github.com/A00476407/DjangoDemo/blob/main/Screenshots/class_POST_result2.png?raw=true)

## SEARCH (Class Based)
- Add a room entry with JSON request body
- URL: localhost:8000/app/classrooms?search={id}
- e.g. localhost:8000/app/classrooms?search=5
![alt text](https://github.com/A00476407/DjangoDemo/blob/main/Screenshots/class_search.png?raw=true)