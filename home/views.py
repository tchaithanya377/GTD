from django.shortcuts import render,redirect
from django.http import HttpResponse
from todo.models import todo, ideas_goals, notes

from datetime import datetime, timedelta
import time
# Create your views here.

def home(request):
    currentDate = time.strftime("%Y-%m-%d")
    if request.method == 'GET':
        do = todo.objects.filter(date = currentDate,complted = False)
        compileted = todo.objects.filter(date = currentDate,complted = True)
        goal = ideas_goals.objects.filter(ideas__isnull=False)
        note = notes.objects.all() 
        return render(request, 'home.html', {'data':do, 'com':compileted, 'goal':goal, 'notes':note})
    return render(request, 'home.html')


def todoupdate(request,pk):
    if request.method == 'POST':
        c = request.POST.get('come')
        todo.objects.filter(pk=pk).update(complted = c)
        return redirect('home')
    return render(request, 'todoupadate.html')

def tomorrowtodo(request):
    next_day = datetime.now()+timedelta(1)
    if request.method == 'GET':
        do = todo.objects.filter(date = next_day,complted = False)
        return render(request, 'tomorrow.html', {'tomorrow':do})
    return render(request, 'tomorrow.html')

def weektodo(request):
    currentDate = datetime.now()
    week_day = datetime.now()+timedelta(7)
    week = week_day.strftime("%Y-%m-%d")
    if request.method == 'GET':
        do = todo.objects.filter(date__range = [currentDate, week_day ])
        return render(request, 'week.html', {'week':do})
    return render(request, 'week.html')

def completed(request):
    if request.method == 'GET':
        completed = todo.objects.filter(complted = True)
        return render(request, 'completed.html', {'complete':completed})
    return render(request, 'completed.html')

def successful(request):
    return render(request,'successfully.html')