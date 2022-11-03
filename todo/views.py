from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from .models import todo, notes
from .forms import todoform, todoupdate
# Create your views here.

class todo(CreateView):
    model = todo
    form_class = todoform
    template_name = 'today.html'
    success_url = '/'
