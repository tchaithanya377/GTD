
from django.urls import path
from .views import *

urlpatterns = [
    path('createtodo',todo.as_view()),
    path('update/<pk>',todoupdates.as_view(model = todo), name= 'update')
]
