from django.http import HttpResponse, HttpRequest
from django.http.response import HttpResponseRedirect
from django.template import loader


from . import models, forms


def render_homepage(request: HttpRequest) -> HttpResponse:
    content = {"boards": models.Board.objects.all()}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(content, request))


def render_board(request: HttpRequest, board_shortcut: str) -> HttpResponse:
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


def render_post(request: HttpRequest, board_shortcut: str) -> HttpResponse:
    template = loader.get_template("post.html")
    return HttpResponse(template.render({"form": forms.ThreadPostForm, "board": board_shortcut}, request))


def new_thread(request: HttpRequest, board_shortcut: str) -> HttpResponse:
    board = models.Board.objects.all().filter(shortcut=board_shortcut).first()
    if request.method == "POST":
        form = forms.ThreadPostForm(request.POST)
        if form.is_valid():
            thread = models.Thread(related_board=board, **form.cleaned_data)
            thread.save()
            return HttpResponseRedirect(f"/{board_shortcut}")
        else:
            return HttpResponse(f"Form invalid")
    else:
        return HttpResponse(f"Unallowed method")
