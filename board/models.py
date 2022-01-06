from django.db import models
from django.utils import timezone


class Board(models.Model):
    name = models.CharField(max_length=30)
    shortcut = models.CharField(unique=True, max_length=10, primary_key=True)
    short_description = models.CharField(max_length=30, default=None)

    def __str__(self) -> str:
        return f"#{self.id_board} {self.name}"


class Message(models.Model):
    id_message = models.BigAutoField(primary_key=True)
    author = models.CharField(max_length=40, default="Аноним")
    content = models.CharField(max_length=300)
    picture_url = models.CharField(max_length=150, default=None)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"MSG: #{self.id_message} by {self.author}"


class Thread(Message):
    id_thread = models.BigAutoField(primary_key=True)
    related_board = models.OneToOneField(Board, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"THREAD: #{self.id_thread} by {self.author}"


class ThreadResponse(Message):
    id_response = models.BigAutoField(primary_key=True)
    parential_thread = models.OneToOneField(Thread, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"RESP: #{self.id_response} by {self.author} to {self.parential_thread}"
