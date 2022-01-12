from django.urls import path, re_path


from . import views

urlpatterns = [
    path("", views.render_homepage, name="Main Page"),
    re_path(r"(?P<board_shortcut>[a-zA-Z]{1,2})/process-thread/$", views.new_thread, name="Create new thread"),
    re_path(r"(?P<board_shortcut>[a-zA-Z]{1,2})/new-thread/$", views.render_post, name="New Thread"),
    re_path(r"(?P<board_shortcut>[a-zA-Z]{1,2})/$", views.render_board, name="Render concrete board"),
]
