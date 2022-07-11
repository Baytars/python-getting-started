from django.shortcuts import render
from django.http import HttpResponse
import requests, json

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def p2(request):
    url = json.loads(request.body)['url']
    print(url)
    print(request.body)
    with requests.get(url) as res:
        return HttpResponse(res, status = res.status_code)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
