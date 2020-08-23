#######################
OscarDropship
#######################

Build Dropshipping website with Django Oscar.

Development
###########

* Create database
```python3
CREATE DATABASE od;
CREATE USER od WITH PASSWORD 'password';
ALTER ROLE od SET client_encoding TO 'utf8';
ALTER ROLE od SET default_transaction_isolation TO 'read committed';
ALTER ROLE od SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE od TO od;   
\q
```

* Install dependencies
```
pip install -r config/requirements/base.txt
pip install -r config/requirements/local.txt
```

* Migrate database using `python manage.py migrate`

* Create super user `python manage.py createsuperuser`

* Run development server `python manage.py runserver`

  
Oscar - eCommerce
#################

* Populate countries `python manage.py oscar_populate_countries`