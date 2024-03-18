from django.db import models

from users.models import CustomUser


class Wallet(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    value = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}: {self.value} руб'


class Category(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Note(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    value = models.IntegerField(null=False)
    date_note = models.DateField(null=True)

    def __str__(self):
        return f'{self.category}: {self.value} руб'


class Plan(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
    type = models.CharField(max_length=30)
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return f'{self.type}: {self.value}'
