from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name = "todos"),
    path("add/", views.add, name= "add"),
    path("toggle/<int:todo_id>/", views.toggle_todo, name="toggle_todo"),
    path("delete/<int:todo_id>/", views.delete_todo, name="delete_todo"),
]