from django.urls import path
from . import views

urlpatterns = [
    path('director/', views.director_list),
    path('director/<int:id>/', views.director_detail),
    path('', views.movie_list),
    path('<int:id>/', views.movie_detail),
    path('review/', views.review_list),
    path('review/<int:id>/', views.review_detail),
]

