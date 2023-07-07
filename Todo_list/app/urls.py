from django.urls import path
from . import views

urlpatterns =[
    path('',views.todo_list, name='todo_list'),
    path('create/',views.create_Todo,name='create_todo'),
    path('complete/<int:todo_id>/', views.completed, name='complete_todo'),
    path('edit/<int:todo_id>/',views.edit_todo , name='edit_todo'),
    path('delete/<int:todo_id>/',views.delete_todo , name='delete_todo'),

]