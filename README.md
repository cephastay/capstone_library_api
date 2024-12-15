# Library Management System API
   __Overview__  
```
The Library Management System API provides a set of RESTful endpoints to manage books, users, reviews, and genres. 
    
It supports functionalities like browsing books, borrowing and
returning books, writing reviews, and other database CRUD actions on books.
```
__Requirements__    

    The required software/tool and libraries you will need for the  
    API to function properly are listed below. The bullets are  
    hyperlinked to the respective tool website.

- [Python 3.8+]()
- [Django 3.0+]()
- [Django REST Framework]()
- [SQLite (for development)]() or [MySQL (for production)]()

#
__Installation__    

The instructions outlined here should be followed through   
in your command line terminal. These are done with `bash` shell.

_*Clone the repository from github:*_ 
```bash
$ git clone https://github.com/cephstay/capstone_library_api.git
```

_*Move into the automatically created directory: `capstone_library_api`*_
```bash
$ cd capstone_library_api
```

_*Activate the virtual environment `library_venv`*_
```bash
$ source library_venv/bin/activate
```

_*Install the library packages in the `requirements.txt` file*_
```bash
$ pip install -r requirements.txt
```

_*Set up your database connection settings in the `.env` file*_

- [Instructions Here]()

_*Migrate the database*_
```bash
$ python manage.py migrate
```

_*Create a SuperUser (Optional)*_
```bash
$ python manage.py createsuperuser --username --email --password
```

_*Start the Development Server*_
```bash
$ python manage.py runserver
```

The API should now be running at `https://127.0.0.1:8000`

# 

# Database Schema and Table Relationships


#

# User EndPoints

# Testing of User End Points with PostMan
Click on the highlighted links to be redirected to a google drive with the images of the test cases

- [GET /users/user_id/](https://drive.google.com/file/d/1aUjmbQx9c5QgMDF_K88-RU-VZOP726rW/view?usp=sharing)

- [POST /users/new/](https://drive.google.com/file/d/1FsZpW11ak1G1T4LE9By9qJLixtbPnCnS/view?usp=sharing)

- [PUT /users/3/update/](https://drive.google.com/file/d/1kV-EO2m-n0BgEJz3U5ZpAvZY0ynX0oRa/view?usp=sharing) - Success

-  [PUT /users/3/update/](https://drive.google.com/file/d/1aLduaHX7dzdsQvXJ499trvHvYKSXVwsp/view?usp=sharing) -Forbidden

```
Only four endpoints were tested.

1. The GET method to retrieve information about a particular user

2. The POST method for creating a new user

3. The PUT method for updating information about the User

The only method which required authentication was the PUT method
```