from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    s="<h1>This is chim WEbsite link.dont dare To play with it!!!<h1/>"
    return HttpResponse(s)
