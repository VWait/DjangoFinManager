from django.db import models

from django.contrib.auth.models import User


class Buffer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.FloatField(default=0)
    expected_value = models.FloatField(default=0)

    def __str__(self):
        return f'Счёт - {self.value} руб'


class CategoryType(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f'Категория "{self.name}"'


class Category(models.Model):
    buffer = models.ForeignKey(Buffer, on_delete=models.CASCADE)
    category_type = models.ForeignKey(CategoryType, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    date_start = models.DateField()
    date_end = models.DateField(null=True)
    period = models.DurationField()
    expected_value = models.FloatField(null=True)


class Note(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    value = models.FloatField()
