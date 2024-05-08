from django.db import models

from django.contrib.auth.models import User
from django.db.models import QuerySet

from typing import Optional


class Buffer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    value = models.FloatField(default=0)
    expected_value = models.FloatField(default=0)

    def __str__(self):
        return f'Счёт - {self.value} руб'

    @staticmethod
    def get_buffer_by_user(user: User) -> Optional['Buffer']:
        query_set = Buffer.objects.filter(user=user)
        if query_set:
            return query_set[0]
        return None

    def __get_categories_by_type(self, type_name: str) -> QuerySet:
        category_type = CategoryType.get_category_type_by_name(type_name)

        if not category_type:
            return QuerySet()

        query_set = Category.objects.filter(buffer=self, category_type=category_type)

        return query_set

    def get_categories_income(self):
        return self.__get_categories_by_type('Доходы')

    def get_categories_expenses(self):
        return self.__get_categories_by_type('Расходы')


class CategoryType(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f'Категория "{self.name}"'

    @staticmethod
    def get_category_type_by_name(name: str) -> Optional['CategoryType']:
        query_set = CategoryType.objects.filter(name=name)
        if query_set:
            return query_set[0]
        return None


class Category(models.Model):
    buffer = models.ForeignKey(Buffer, on_delete=models.CASCADE)
    category_type = models.ForeignKey(CategoryType, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    date_start = models.DateField()
    date_end = models.DateField(null=True)
    period = models.DurationField()
    expected_value = models.FloatField(null=True)

    def get_fields_for_table(self) -> dict:
        return {
            'name': self.name,
            'value': self.expected_value,
            'date': self.date_start
        }


class Note(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    value = models.FloatField()
