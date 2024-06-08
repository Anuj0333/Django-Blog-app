from django.urls import path
from . import views
appname = "users"
urlpatterns = [
    path("register/", views.register,name='register'),
    path("profile/", views.profile,name='profile'),
]