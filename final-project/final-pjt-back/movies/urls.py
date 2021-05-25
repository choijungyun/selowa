from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movies),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/reviews/', views.reviews),
    path('recommend/', views.recommend),
    path('<int:my_pk>/like/', views.my_movie_like),
]

