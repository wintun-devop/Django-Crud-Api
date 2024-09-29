#https://stackabuse.com/creating-a-rest-api-with-django-rest-framework/

#create django env on ubuntu
python3.11 -m venv django_crud_env
soucre django_crud_env/bin/activate

#Install necessary packages
pip install django django_rest_framework
pip freeze > requirements.txt

#Project Create
#django-admin startproject YourProjectName
django-admin startproject djangocrud
cd djangocrud
django-admin startapp apis

#Database and app setting
djangocrud/djangocrud/setting
# AppSetting
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     #developer add
    'rest_framework',
    'apis'
]

# Database Setting
# developer add
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_crud_api',
        'USER': 'dbadmin',
        'PASSWORD': 'Abc123Abc123',
        'HOST': '172.18.0.2',
        'PORT': '5432',
    }
}

# Start Initialize the App and Database

python3 manage.py migrate
python3 manage.py createsuperuser

# initial Server Run
python3 manage.py runserver

# Create Model

djangocrud/apis >> create model

# Create your models here.
from django.db import models
import uuid
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=200,unique=True)
    price = models.FloatField()
    quantity = models.PositiveIntegerField()

# Admin Register to model (apis/admin.py)

from django.contrib import admin
from .models import Product
admin.site.register(Product)
python3 manage.py makemigrations
python3 manage.py migrate

# create ModelSerializer (apis/serializers.py),



# create Views ((apis/views.py))

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import YourItemSerlizer
from .models import YourItemModel

# Register end-point url (djangocrud/djangocrud/urls.py)

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('apis.urls'))
]

# create Urls (apis/urls.py)
from django.urls import path
from .views import YourView

urlpatterns = [
    #main endpoint
    path('products/', YourView.as_view())
]


