from django.contrib import admin
from users.models import User


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, AuthorAdmin)
