from django.urls import path
from . import views
from django.urls import path
from .views import chat_api


     
urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("enter/", views.enter, name="enter"),
    path("ai/", views.ai, name="ai"),
    path("ai/chat/", views.chat_api, name="chat_api"),
]


