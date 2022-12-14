from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request):
    return JsonResponse({'id':1,'name':'Vignesh','Course':'Django with react'})