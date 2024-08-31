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

# Django Project #
Creating project: `django-admin startproject learning_project`

Creating app: `python manage.py startapp employees`

Running server: `python manage.py runserver 0.0.0.0:8000`

Make Migrations: `python manage.py makemigrations employees`

# Associating With Uwsgi #
sudo yum update && sudo yum upgrade -y

sudo yum groupinstall "Development Tools"
sudo yum install python3-devel

pip install --upgrade wheel

pip install uwsgi

# Associate with Jenkins #

sudo yum update -y 

sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
