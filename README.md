# learning-project-dj
Learning Django A-Z

###### Getting ready with Python ########
# Install python 3.11.9
Use Python windows installer
Set the installed version in $PATH variable 

# Create virtual env
python -m venv learning_project_dj 

# Activate virtual env
learning_project_dj\Scripts\activate.bat

# Deactivate virtual env
deactivate

##### Django Project ########
Creating project: `django-admin startproject learning_project`
Creating app: `python manage.py startapp employees`
Running server: `python manage.py runserver`
Make Migrations: `python manage.py makemigrations employees`