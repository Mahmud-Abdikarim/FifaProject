from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = 'Players' 

urlpatterns = [
    path('players/', views.homepage, name='homepage'),
    path('players/<int:request_year>/', views.homepage, name='homepage'),
    path('players/<int:request_year>/<slug:query>/', views.homepage, name='homepage'),
    path('clubs/', views.clubs, name='clubs'),
    path('clubs/<int:request_year>/', views.clubs, name='clubs'),
    path('clubs/<int:request_year>/<slug:query>/', views.clubs, name='clubs'),
    path('player_detail/<int:player_id>/', views.player_detail, name='player_detail'),
    path('player_detail/<int:request_year>/<int:player_id>/', views.player_detail, name='player_detail'),
    path('club_detail/<int:request_year>/<int:request_club_id>/', views.club_detail, name='club_detail'),
    path('club_edit/',views.club_edit, name='club_edit')

]
