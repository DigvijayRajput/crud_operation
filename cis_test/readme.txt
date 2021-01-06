
1. install python 3.7

2. To access the project, it is better to use a virtual directory as it will keep the django version in your computer and the one used in this project seperate.

    - Commands to use virtual directory in linux/ubuntu enviroment:

        virtualenv env_name                 # create virtual enviroment
        source env_name/bin/activate        # activate virtual enviroment
        pip install -r requirements.txt     # install requirements.txt

3. Create test databse by running the django migration using below Command it will create sqlite3 databse

    python manage.py migrate

4. After migration Create superuser using below command

    python manage.py createsuperuser

5. Now you can run the server by this command:

    python manage.py runserver


6. Check the following links after server runs:

    http://127.0.0.1:8000
    http://127.0.0.1:8000/admin/                # For admin use
    http://127.0.0.1:8000/register/             # To register the user
    http://127.0.0.1:8000/user_login/           # To login the user
    http://127.0.0.1:8000/logout/               # 
    http://127.0.0.1:8000/product/
    http://127.0.0.1:8000/get_products/
    http://127.0.0.1:8000/update_products/pk/
    http://127.0.0.1:8000/delete/pk/
