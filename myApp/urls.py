from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name = "todos"),
    path("add/", views.add_todo, name= "add_todo")
]