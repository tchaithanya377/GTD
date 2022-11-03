from django.shortcuts import render
from todo.forms import todoform, done
from django.http import HttpResponse
from todo.models import todo
import time
# Create your views here.

def home(request):
    currentDate = time. strftime("%Y-%m-%d")
    if request.method == 'GET':
        do = todo.objects.filter(date = currentDate)
        compileted = todo.objects.filter(complted = True)
        return render(request, 'home.html', {'data':do, 'com':compileted})
    else:
        don = done()
        if don.is_valid():
            don.save()
    return render(request, 'home.html',{'form':don})

def todoc(request):
    if request.method == 'POST':
        form = todoform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('created')
    else:
        form = todoform()
    return render(request, 'today.html',{'form':form})