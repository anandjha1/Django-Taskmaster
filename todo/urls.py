from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_todo, name='create_todo'),
    path('edit/<int:id>/', views.edit_todo, name='edit_todo'),
    path('delete/<int:id>/', views.delete_todo, name='delete_todo'),
    path('complete/<int:id>/', views.complete_todo, name='complete_todo'),
]