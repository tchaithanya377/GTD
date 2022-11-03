
from django.urls import path
from .views import *

urlpatterns = [
    path('createtodo',todo.as_view(), name="createtodo"),

]