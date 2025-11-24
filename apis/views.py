from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def health(request):
    return JsonResponse({"message":"Health check"})
