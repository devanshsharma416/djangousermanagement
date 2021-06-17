from django.urls import path, include
from .views import home, delete

urlpatterns = [
    path('', home, name = 'home'),
    path('delete/<str:pk>', delete, name = 'delete')

]