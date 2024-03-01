from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    tags=['one','two', 'three','four']
    return render(request, 'index.html')


def cartPage (request):
    return render(request,'cart.html')

def createMember(request):
    return render(request, 'createmember.html')