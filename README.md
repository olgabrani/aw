#Athens Warriors 

##Installation
Depending on your system, check that you have python-pip and virtualenvwrapper
installed.
If not, install them with:

```
# Install python-pip package manager
$ apt-get install python-pip

# Install virtualenvwrapper
$ pip install virtualenvwrapper
```

Create a virtualenv, and activate it:
```
# Create virtualenv
$ mkvrirtualenv aw

# Activate virtualenv
$ workon aw
```
Install some necessary packages and libraries:
```
$ apt-get install python-dev libjpeg-dev zlib1g-dev
```

Install requirements:
```
$ pip install -r requirements.txt
```

Create database:

```
$ python manage.py syncdb
$ python manage.py migrate
```

During database creation, you will be prompt to create a superuser.


##Using Docker

Dockerfile will create an empty database populated with a superuser with:

username: admin
password: 1234

Don't forget to change the password after the installation.


