from django.urls import path


from . import views

urlpatterns = [
    path("", views.render_homepage, name="Main Page"),
    path("<str:board_shortcut>/process-thread", views.new_thread, name="Create new thread"),
    path("<str:board_shortcut>/new-thread", views.render_post, name="New Thread"),
    path("<str:board_shortcut>", views.render_board, name="Render concrete board"),
]
