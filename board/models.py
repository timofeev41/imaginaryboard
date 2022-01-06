from django.db import models
from django.utils import timezone


class Board(models.Model):
    id_board = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    shortcut = models.CharField(unique=True, max_length=10)


class Message(models.Model):
    id_message = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=40, default="Аноним")
    content = models.CharField(max_length=300)
    picture_url = models.CharField(max_length=150, default=None)
    date_created = models.DateTimeField(default=timezone.now())


class Thread(Message):
    id_thread = models.IntegerField(primary_key=True)
    related_board = models.OneToOneField(Board, on_delete=models.CASCADE)


class ThreadResponse(Message):
    id_response = models.IntegerField(primary_key=True)
    parential_thread = models.OneToOneField(Thread, on_delete=models.CASCADE)
