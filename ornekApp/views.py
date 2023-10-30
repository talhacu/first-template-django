from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


def ornekep(request):
    return HttpResponse("secondapp bitch")

def keepgoing(request):
    return HttpResponse("bro you sick")