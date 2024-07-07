from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  return HttpResponse("Hello, world!")


def brian(request):
  return HttpResponse("Hello, Brain!")

def david(request):
  return HttpResponse("Hello, David!")

def greet(request, name):
  return HttpResponse(f"Hello, {name}!")