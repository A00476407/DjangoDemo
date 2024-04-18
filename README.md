# Django Assignment
This is a Django application which is connected to a remote MySQL database and provides REST API to access the data.

# Create virtual environment
1. Navigate to the `venv/Scripts/` directory
2. Run `activate.bat`

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
## GET API
- Get a list of available hotels room
- URL: localhost:8000/app/roomlist
![alt text](https://github.com/A00476407/django_demo/blob/main/Screenshots/GET.png?raw=true)

## POST API
- Add a room entry with JSON request body
- URL: localhost:8080/hotels
```JSON
{
  "price": 200,
  "type_id": 1
}
```
![alt text](https://github.com/A00476407/django_demo/blob/main/Screenshots/POST.png?raw=true)
![alt text](https://github.com/A00476407/django_demo/blob/main/Screenshots/POST_result.png?raw=true)
![alt text](https://github.com/A00476407/django_demo/blob/main/Screenshots/POST_result2.png?raw=true)
