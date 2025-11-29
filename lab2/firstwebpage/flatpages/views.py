from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

# def home(request):
#     return HttpResponse(u'Привет, Мир!', content_type="text/plain; charset=utf-8")
# def home(request):
#     return HttpResponse("Привет, Мир!")
#
#
# def hello(request):
#     return HttpResponse("Привет, Мир!")

from django import template


# def home(request):
#     return render(request, 'templates/index.html')
def home(request):
    return render(request, 'templates/static_handler.html')