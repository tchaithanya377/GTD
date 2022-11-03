from django.shortcuts import render
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

# class todoupdates(UpdateView):
#     model = todo
#     # form_class = todoupdate
#     fields = ['task','date','complted']
#     template_name = 'todoupdate.html'
#     success_url = '/'
    

class todoupdates(UpdateView):
    model = notes
    fields = ['title']
    template_name_suffix = '_update_form'
    template_name = 'todoupdate.html'
