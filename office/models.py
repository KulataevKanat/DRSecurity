from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext_lazy as _
from DrJwt.models import BaseModel
from office.managers import UserAccountManager


class User(BaseModel, AbstractUser):
    id = models.AutoField(primary_key=True)
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, default=1)
    email = models.EmailField(max_length=50, unique=True)

    REQUIRED_FIELDS = ['groups_id', 'email']

    objects = UserAccountManager()

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    class Meta:
        db_table = 'api_user'
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')


class Table(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Стол')
        verbose_name_plural = _('Столы')
