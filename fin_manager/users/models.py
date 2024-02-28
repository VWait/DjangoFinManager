from django.db import models


class User(models.Model):
    login = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.login
