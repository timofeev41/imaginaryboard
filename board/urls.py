from django.urls import path


from . import views

urlpatterns = [
    path("", views.render_homepage, name="Main Page"),
    path("<str:board_shortcut>", views.render_board, name="Render concrete board"),
]
