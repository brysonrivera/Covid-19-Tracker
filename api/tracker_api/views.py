from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
import json
# Create your views here.
@api_view(['GET'])
def cases_per_100k(request):
    zip = request.query_params.get('zip')
    f = open('zip_to_county.json')
    zips = json.load(f)
    if zip in zips:
        county = zips[zip]
        res = requests.get(f'https://data.cdc.gov/resource/3nnm-4jni.json?county={county} County').json()[0]
        return Response({'covid_cases_per_100k': res['covid_cases_per_100k']})
    return Response("Invalid zip code", status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def hesitancy_rate(request):
    return HttpResponse("Hesitancy rate data should be returned")
