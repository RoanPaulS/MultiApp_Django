from django.shortcuts import render
from django.http import HttpResponse
import datetime

def tellMeTime(request):
    time = datetime.datetime.now()
    return HttpResponse("<h1>Hi the time is : "+str(time)+"</h1>")
