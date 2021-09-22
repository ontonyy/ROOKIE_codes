from django.http import HttpResponse
import requests


def hello(request):
    return HttpResponse("Hello world")


r = requests.get('')

