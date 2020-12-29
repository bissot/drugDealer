from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'drugdealergame'),    # calls the function home in the views.py
    path('about/', views.about, name = 'aboutgame'),    # calls the function about in the views.py
    path('rules/', views.rules, name = 'rules'),	#calls the function rules in views.py
    path('lobby/<str:gameroom_code>/', views.lobby, name = 'lobby'),	#calls the function lobby in views.py
    path('game/<str:gameroom_code>/', views.game, name = 'game'),	#calls the function game in views.py
]
