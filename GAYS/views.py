from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return JsonResponse({"message":'Okay Gays are here'})

