from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Room(models.Model):
    name = models.CharField(max_length=218)
    participants = models.ManyToManyField(User, related_name='rooms')


# class Message(models.Model):
#     room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    username = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
