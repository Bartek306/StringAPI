import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def string(request):
    return None



