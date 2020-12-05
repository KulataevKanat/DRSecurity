from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from office.models import User, Table

admin.site.register(User)
admin.site.register(Table)

