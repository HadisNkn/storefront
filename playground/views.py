# My first view in the playground app
from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    return HttpResponse('Hello World')







# Create your views here.
# request -> response
# request handler
# actions