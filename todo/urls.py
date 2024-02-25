from django.urls import path ,include
from . import views

app_name = 'todo'

urlpatterns = [
    path('',views.index,name="index"),
    path('<int:pk>/',views.detail,name="detail"),
    path('create_task/',views.create_task,name="create_task"),
    path('delete_task/<int:pk>/',views.delete_task,name="delete_task"),

]

