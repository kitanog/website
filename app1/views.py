from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("""
    Hi, this is my first App (app1)
    It will include some information about my site
    """)

def testview(request, num):
    response = "This is the result of your testview in app1 num: %s"
    return HttpResponse(response % num)