from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("register/",views.register,name="register"),
    path("login/",views.user_login,name="login"),
    path("logout/",views.user_logout,name="logout"),
    path("",views.profile,name="profile"),
    path("edit/",views.edit_profile,name="edit_profile"),
    path("edit/pass_change/",views.pass_change,name="pass_change"),
    path("edit/pass_change2/",views.pass_change2,name='pass_change2'),
]
