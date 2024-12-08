#Library Management System API
Overview
The Library Management System API provides a set of RESTful endpoints to manage books, users, reviews, and categories. 
It supports functionalities like browsing books, borrowing and returning books, writing reviews, and adding new books.

Requirements
-Python 3.8+
-Django 3.0+
-Django REST Framework
-SQLite (for development) or MySQL (for production)

Installation
Clone the repository:

```bash
Copy code
git clone https://github.com/cephstay/capstone_library_api.git
cd capstone_library_api
Set up a virtual environment:


Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install the dependencies:


Copy code
pip install -r requirements.txt
Migrate the database:


Copy code
python manage.py migrate
Create a superuser (optional):


Copy code
python manage.py createsuperuser
Start the development server:


Copy code
python manage.py runserver
The API should now be running at http://127.0.0.1:8000.

