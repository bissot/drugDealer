from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'drugdealergame'),    # calls the function home in the views.py
    path('about/', views.about, name = 'aboutgame'),    # calls the function home in the views.py
]
