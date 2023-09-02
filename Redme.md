#https://stackabuse.com/creating-a-rest-api-with-django-rest-framework/

#create django env on ubuntu
python3.11 -m venv django_crud_env
soucre django_crud_env/bin/activate

#Install necessary packages
pip install django
pip install django_rest_framework
pip freeze > requirements.txt