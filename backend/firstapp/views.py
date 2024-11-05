from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request,month):
#     return HttpResponse(month)
def index(request,year,month):   
    if month =='jan':
      return HttpResponse('learn django')
    elif month == 'feb':
      return HttpResponse('learn Django URLs')
    else:
       return HttpResponse('The URL you entered is not found')
 

# def index(request):
#     return HttpResponse('learn python')
# def index1(request):
#     return  HttpResponse('learn django')
    

