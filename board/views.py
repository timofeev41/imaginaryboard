from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, loader, context


def render_homepage(request) -> HttpResponse:
    template = loader.get_template("index.html")
    return HttpResponse(template.render({}, request))
