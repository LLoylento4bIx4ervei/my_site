from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1> Hello World</h1>')

def about_author(request):
    return HttpResponse('<h1>About Author</h1>')
