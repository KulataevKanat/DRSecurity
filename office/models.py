from django.db import models
from django.contrib.auth.models import AbstractUser, Group

from DrJwt.models import BaseModel


class User(AbstractUser):
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, default=1)
    email = models.EmailField(max_length=50, unique=True)

    REQUIRED_FIELDS = ['groups_id', 'email']

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name


class Table(BaseModel):
    name = models.CharField(max_length=20, blank=True)
