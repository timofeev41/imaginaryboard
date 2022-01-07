from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, loader, context


from . import models


def render_homepage(request) -> HttpResponse:
    content = {"boards": models.Board.objects.all()}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(content, request))


def render_board(request, board_shortcut: str) -> HttpResponse:
    board = models.Board.objects.all().filter(shortcut=board_shortcut).first()
    if board is None:
        return HttpResponse("wtf")
    content = {
        "threads": models.Thread.objects.filter(related_board=board_shortcut).all(),
        "name": board_shortcut,
        "board_data": board,
    }
    template = loader.get_template("board.html")
    return HttpResponse(template.render(content, request))
