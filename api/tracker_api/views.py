from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def num_cases(request):
    return HttpResponse("Num cases data should be returned")

@api_view(['GET'])
def hesitancy_rate(request):
    return HttpResponse("Hesitancy rate data should be returned")
