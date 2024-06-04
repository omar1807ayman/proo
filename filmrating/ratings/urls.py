from django.urls import path
from . import views

urlpatterns = [
    path('', views.film_list, name='film_list'),
    path('film/<int:film_id>/', views.film_detail, name='film_detail'),
    path('my_ratings/', views.my_ratings, name='my_ratings'),
]
