from django.shortcuts import render
from django.http import HttpResponseRedirect
from newapp.models import *

def index(request):
	counterget = Counter.objects.all()[:1].get()
	countget = counterget.count
	countget = countget + 1
	counterget.count = countget
	counterget.save()
	return render(request, 'demoapp2/index1.html', {'countget': countget%3})
