from django.urls import path
from . import views

urlpatterns = [
    path('', views.users),
    path('login/', views.user_login),
]