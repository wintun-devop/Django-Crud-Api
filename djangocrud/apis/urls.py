from django.urls import path
from .views import ProductViews

urlpatterns = [
    path('products/', ProductViews.as_view()),
    path('products/<str:id>', ProductViews.as_view())
]