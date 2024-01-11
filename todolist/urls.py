from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_todo', views.new_todo, name='new-todo'),
    path('complete/<int:id>', views.complete, name='complete'),
    path('delete/<int:id>', views.delete, name='delete'),
]
