from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexTodo, name='todo'),
    path('<int:id>', views.detailTodo, name='todo_detail'),
    path('create', views.createTodo, name='todo_create')
]
