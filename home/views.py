from django.shortcuts import render,redirect
from todo.forms import todoform, todoupdate
from django.http import HttpResponse
from todo.models import todo
from django.views.generic.edit import UpdateView
import time
# Create your views here.

def home(request):
    currentDate = time. strftime("%Y-%m-%d")
    if request.method == 'GET':
        do = todo.objects.filter(date = currentDate,complted = False )
        compileted = todo.objects.filter(complted = True)
        return render(request, 'home.html', {'data':do, 'com':compileted})
    return render(request, 'home.html')


def todoupdate(request,pk):
    if request.method == 'POST':
        c = request.POST.get('come')
        print(c)
        todo.objects.filter(pk=pk).update(complted = c)
        return redirect('home')
    return render(request, 'todoupadate.html')
