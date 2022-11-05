
from django.urls import path
from .views import *

urlpatterns = [
    path('createtodo',todo.as_view(), name="createtodo"),
    path('createnotes',notescreate.as_view(), name="createnotes"),
    path('notes',notes.as_view(), name="notes"),
    path('updatenotes/<pk>',updatenotes.as_view(), name="updatenotes"),
    path('updatetodo/<pk>',updatetodo.as_view(), name="updatetodo"),
    path('createideas',ideascreate.as_view(), name="createideas"),
    path('updateideas/<pk>',ideasupdate.as_view(), name="updateideas"),
    path('creategoals',goalscreate.as_view(), name="creategoals"),
    path('updategoals/<pk>',goalsupdate.as_view(), name="updategoals"),

]