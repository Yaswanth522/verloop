# libraries
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import json

# Global variabless
AUTHORIZATION_KEY = "AIzaSyCOD3KvY2DDzEfel-NZ_LKIWXr86EF_EUw"


# function to get coordinates based on address given to api
@api_view(['GET', 'POST'])
def getAddressDetails(request):
    # for both GET and POST requests coordinates of address is response(like google Geolocation api)
    if(request.method == "POST" or request.method == "GET"):
        data = JSONParser().parse(request)  # parsing the data of api request
        # checking whether requested output format is json or xml and giving response accordingly.
        if(data["output_format"] == "json"):
            return JsonResponse(googleApi(data["address"], data["output_format"]), status=status.HTTP_200_OK)
        elif(data["output_format"] == "xml"):
            return Response(googleApi(data["address"], data["output_format"]), status=status.HTTP_200_OK)
    return JsonResponse(status=status.HTTP_400_BAD_REQUEST)  # user not using GET or POST to hit API


# hitting google Geolocation API to get coordinates
def googleApi(address, format):
    # sending post request with address and authorization key
    response = requests.post("https://maps.googleapis.com/maps/api/geocode/json?address=" + formatter(address) + "&key=" + AUTHORIZATION_KEY)
    data = json.loads(response.content)  # converting web response into json to parse it
    lat = data["results"][0]["geometry"]["location"]["lat"]  # parsing latitude
    lng = data["results"][0]["geometry"]["location"]["lng"]  # parsing longitude

    # creating dictionaries to convert into json or xml as per output format
    if(format == "json"):
        responseDict = {
            "coordinates": {
                "lat": float(str(lat)[:8]),
                "lng": float(str(lng)[:8])
            },
            "address": address
        }
    elif(format == "xml"):
        responseDict = {
            "address": address,
            "coordinates": {
                "lat": float(str(lat)[:8]),
                "lng": float(str(lng)[:8])
            }
        }
    return responseDict


# converting given address into google geolocation api supported format
def formatter(address):
    return address.replace(" ", "+")
