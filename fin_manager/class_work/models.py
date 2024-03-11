from django.db import models


class Message(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
