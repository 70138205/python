from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('learn python')
def index1(request):
    return  HttpResponse('learn django')
    

