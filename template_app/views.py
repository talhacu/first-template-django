from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


def index(request):
    return HttpResponse("Main Page")

def tahino(request):
    return HttpResponse("tahini tahino")