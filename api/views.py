from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from datetime import datetime
import pytz


def Retrieve_api(request):
  response_data = {
    "registered_email" : "nnannamari@gmail.com",
    "current_date" : datetime.now(pytz.utc).isoformat(),
    "repo_url" : "https://github.com/NnannaMari09033/HNG-.git"
  }
  return JsonResponse(response_data, status=200)