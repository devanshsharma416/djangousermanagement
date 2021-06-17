from django.urls import path
from dictionary import views

urlpatterns = [
    path('', views.dict, name = 'dict'),
    path('word', views.word, name = 'word')

]