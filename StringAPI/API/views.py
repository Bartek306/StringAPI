import json

from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def string(request):
    body_unicode = request.body.decode('utf-8')
    print("body = ", body_unicode)
    if body_unicode == "":
        return HttpResponseNotFound("Request body is empty")
    body = json.loads(body_unicode)
    data = body['message']

    upper = 0
    lower = 0
    special = 0
    for letter in data:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
        elif not letter.isalnum():
            special += 1

    response = {'upper': upper, 'lower': lower, 'special': special}
    return HttpResponse(json.dumps(response), content_type='application/json')
    


