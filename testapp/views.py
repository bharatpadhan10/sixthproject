from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_view(request):
    return HttpResponse('first view')

def second_view(request):
    return HttpResponse('second view')

def third_view(request):
    return HttpResponse('third view')