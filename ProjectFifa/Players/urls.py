from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('added/', views.homepage_added, name='added'),
    path('free/', views.homepage_free, name='free'),
    path('loaned/', views.homepage_free, name='loaned'),
    path('added/', views.homepage_free, name='added'),
    path('clubs/', views.clubs, name='clubs'),
    path('player_detail/<int:request_year>/<int:player_id>/', views.player_detail, name='player_detail'),
    path('club_detail/<int:request_year>/<int:request_club_id>/', views.club_detail, name='club_detail')

]
