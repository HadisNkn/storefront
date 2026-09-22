# My first view in the playground app
from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    return HttpResponse('Hello World')

def calculate():
    x = 1
    y = 2
    return x

def say_hello_2(request):
    x = calculate()
    return render(request, 'hello.html', {'name': 'Hadis'})




# Create your views here.
# request -> response
# request handler
# actions