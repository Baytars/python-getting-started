from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import StreamingHttpResponse
from django.views.decorators.http import require_POST
import requests, json
from django.views.decorators.csrf import csrf_exempt

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def read_in_chunks(res_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 10k."""
    for chunk in res_object.iter_content(chunk_size, decode_unicode=True):
        try:
            yield chunk
        except:
            yield chunk.encode()

@csrf_exempt
@require_POST
def p2(request):
    url = json.loads(request.body)['url']
    print(url)
    with requests.get(url, stream = True) as res:
        return StreamingHttpResponse(read_in_chunks(res))

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
