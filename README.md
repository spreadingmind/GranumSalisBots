# GranumSalisBots



## Local configuration
* switch to branch 'dev'
* create virtualenv + pip install -r requrements.txt
* if using PyCharm to go Settings>Project>Project interpreter and select interpreter from created virtualenv
* install PostgreSQL (https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04)

choose any database and user name;

(until section 'Install Django within a Virtual Environment')
* create gs/settings/local.py for local configurations
add configuration for local database:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<database_name>',
        'USER': '<user_name>',
        'PASSWORD': '<user_password>',
        'HOST': 'localhost',
        'PORT': '',
    }
}

* to check correctness of database run:
- ./manage.py check
- ./manage.py migrate             (to run database scripts - create tables and insert initial data)
- ./manage.py createsuperuser     (to create user)
- ./manage.py runserver           (to start up the application)
* in web browser access   localhost:8000/    and log in as a recently created user    
