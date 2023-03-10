from django.shortcuts import render;
from django.http import HttpResponse

#Create your views here...
def f1(request):
	return HttpResponse("<h1>Hello from DemoApp1 Github</h1><hr />");
def f2(request):
	return HttpResponse("<h1>Hello from DemoApp1 PycharmIDE</h1><hr />");
