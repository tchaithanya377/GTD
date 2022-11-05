from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .models import todo, notes ,ideas, goals
from .forms import todoform,notesform, ideaform, goalsform
# Create your views here.

class todo(CreateView):
    form_class = todoform
    template_name = 'today.html'
    success_url = '/successful'


class notescreate(CreateView):
    form_class = notesform
    template_name = 'notes.html'
    success_url = '/successful'

class ideascreate(CreateView):
    form_class = ideaform
    template_name = 'idea.html'
    success_url = '/successful'

class ideasupdate(UpdateView):
    model = ideas
    form_class = ideaform
    template_name = 'idea.html'
    success_url = '/successful'

class goalscreate(CreateView):
    form_class = goalsform
    template_name = 'goals.html'
    success_url = '/successful'

class goalsupdate(UpdateView):
    model = goals
    form_class = goalsform
    template_name = 'goals.html'
    success_url = '/successful'


class updatenotes(UpdateView):
    model = notes
    form_class = notesform
    template_name = 'notes.html'
    success_url = '/'

class updatetodo(UpdateView):
    model = todo
    form_class = todoform
    template_name = 'today.html'
    success_url = '/'

class notes(ListView):
    model = notes
    template_name = 'notes_list.html'
