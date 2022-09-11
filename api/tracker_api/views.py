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
    zip = request.query_params.get('zip_code')

    with open('zip_to_fips.json') as f:
        zips = json.load(f)
        if zip in zips:
            fips = zips[zip]
            res = requests.get(
                f'https://data.cdc.gov/resource/3nnm-4jni.json?county_fips={fips}').json()
            filtered_res = []
            for entry in res:
                county = f"{entry['county']}, {entry['state']}"
                filtered_res.append({'county': county,
                                     'covid_cases_per_100k': entry['covid_cases_per_100k'],
                                     'date_updated': entry['date_updated']
                                     })
            return Response(filtered_res)

    return Response("Invalid zip code", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def community_level(request):
    zip = request.query_params.get('zip_code')

    with open('zip_to_fips.json') as f:
        zips = json.load(f)
        if zip in zips:
            fips = zips[zip]
            res = requests.get(
                f'https://data.cdc.gov/resource/3nnm-4jni.json?county_fips={fips}').json()[-1]
            county = f"{res['county']}, {res['state']}"
            return Response({'county': county,
                             'community_level': res['covid_19_community_level'],
                             'date_updated': res['date_updated']})

    return Response("Invalid zip code", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def hesitancy_rate(request):
    zip = request.query_params.get('zip_code')

    with open('zip_to_fips.json') as f:
        zips = json.load(f)
        if zip in zips:
            fips = zips[zip]
            if fips[0] == '0':
                fips = fips[1:]
            res = requests.get(
                f'https://data.cdc.gov/resource/q9mh-h2tw.json?fips_code={fips}').json()[-1]
            return Response({'county': res['county_name'],
                             'estimated_hesitance': res['estimated_hesitant']
                             })

    return Response("Invalid zip code", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def hospital_admissions_per_100k(request):
    zip = request.query_params.get('zip_code')

    with open('zip_to_fips.json') as f:
        zips = json.load(f)
        if zip in zips:
            fips = zips[zip]
            res = requests.get(f'https://data.cdc.gov/resource/3nnm-4jni.json?county_fips={fips}').json()
            filtered_res = []
            for entry in res:
                county = f"{entry['county']}, {entry['state']}"
                filtered_res.append({'county': county,
                                     'hospital_admissions_per_100k': entry['covid_hospital_admissions_per_100k'],
                                     'date_updated': entry['date_updated']
                                     })
            return Response(filtered_res)
    return Response("Invalid zip code", status=status.HTTP_400_BAD_REQUEST)
