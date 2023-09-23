## Authors

* Arnaud Norel

## Prerequisites

* PostgreSQL: https://www.postgresql.org/download/ 
    * *Windows only:* add PostgreSQL `bin` directory to your environment variables 
    * *Linux only:* start PostgreSQL: `sudo systemctl start postgresql.service` or `sudo service postgresql start`
* Python 3.8 with pip (`python3.8-pip`), dev tools (`python3.8-dev`) and venv (`python3.8-venv`)
* VSCode (recommanded): https://code.visualstudio.com/download
* Postman (recommanded): https://www.postman.com/downloads/ 

*if you use vscode:*

* Python extension: https://marketplace.visualstudio.com/items?itemName=ms-python.python 

## Installation if you want to use a postgres db

0. Create a postgres user by following this tutorial:  https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04 
    * *Windows only:* you should run `psql -U postgres` instead of `sudo -u postgres psql`
    * Credentials used for this project are : 
    * db_name : sample_db
    * db_user : arno
    * password : EmployeeManagement 
    * *already detailed in docker-compose.yml*
1. clone the repo: `https://github.com/ArnaudNorel95/Okoone_user_management.git`
2. Open the repo with command line and create a venv: `python3.8 -m venv env`
3. Activate the venv: 
    * *Linux:* `source env/bin/activate`
    * *Windows CMD:* `env\Scripts\activate.bat`, 
    * *Windows PS:* `env\Scripts\activate.ps1`
4. (make sure your pip is linked with the venv): `pip --version`, you whould see something like: `.../core/env/lib/site-packages/pip (python 3.8)`
    * Update pip: `python -m pip install --upgrade pip`
5. Install requirements.txt: `pip install -r requirements.txt`
6. Open the folder with VSCode (or your prefeered text editor): `code .`
7. Open control palette (`Ctrl+Shift+P`) and select `Python: Select Interpreter`
8. Choose the venv python interpreter (it should be recommanded one)
9. Close the command line inside VSCode (if it was open) and open a new one using `Ctrl+J`. You should see the venv name in the command line

## CONNECT THE APPLICATION TO SAMPLE DB
* In core/settings.py, either you use the sample.db with all the data already ready then don't need to do the steps 11. and 12.
But You need to uncomment the default database.
Either you use a postgresql db then need to make the migrations (as example for running the tests)
10. Run `python manage.py makemigrations`
11. Run `python manage.py migrate`,
12. Run `python manage.py createsuperuser` and create a Django user to access to the admin side
13. Run `python manage.py runserver` and wait for the application to start

## GET CUSTOMERS ##
14. Open Postman, create a new environment and set the *url* variable to `http://127.0.0.1:8000`
15. In postman, select your environment and use the GET Method at the route /api/customers
16. If you have a response, then the local API is working successfuly !

## CREATE ARTIST ##
17. Still in postman, select your environment and use the POST Method at the route /api/artists/
18. If you have a response, then the local API is working successfuly !

## RUN THE SQL QUERY
19. Please find the file SQLquery in core/ to show how much each customer had spent in the store.

***Warning:*** if you have made modifications to /app/models.py, do not forget to run `python mange.py makemigrations` and `python manage.py migrate` BEFORE running the server

### More

If you install a new python package, do not forget to add it to the `requirements.txt`
