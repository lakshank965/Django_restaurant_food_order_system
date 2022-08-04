# Django_restaurant_food_order_system

## Requirements
- Python 3.10
- Django 4.0

## How to setup project in local
### Step 1
Start MySQL server and Apache server in your local machine.

### Step 2
Go to your local MySQL server and create new Database.

http://localhost/phpmyadmin/

Database name --> food_order_system

### Step 3

Install **mysqlclient**
```powershel
pip install mysqlclient
```

### Step 4
Migrate database.
```powershel
python3 manage.py makemigrations 
```

### Step 5
Import data to Database


1. Go to your local MySQL server http://localhost/phpmyadmin/
2. Go to import tap
3. Chose file from 'Data' folder in project
4. Import

### Step 6
Run application in django server
```powershel
python manage.py runserver
```
Starting development server at http://127.0.0.1:8000/