from django.urls import path, include
from .views import index, create, direct

urlpatterns = [
    path('', index, name = 'index'),
    path('create', create, name = 'create'),
    path('<str:pk>', direct, name = 'direct')
]