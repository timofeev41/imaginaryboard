from django.http import HttpResponse
from django.shortcuts import render



def render_homepage(request) -> HttpResponse:
    return HttpResponse("<h1>Homepage</h1>")
