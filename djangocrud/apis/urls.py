from django.urls import path
# from .old_views import ProductViews
from .views import ProductViews

urlpatterns = [
    path('products/', ProductViews.as_view()),
    path('products/<str:id>', ProductViews.as_view())
]