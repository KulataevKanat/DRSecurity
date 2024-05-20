from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext_lazy as _
from dr_security.models import BaseModel
from api.managers import UserAccountManager


def role_null():
    return Group.objects.get_or_create(name='role_none')[0]


class User(BaseModel, AbstractUser):
    groups = models.ForeignKey(Group, on_delete=models.SET(role_null), null=True, blank=True)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=30, unique=True)

    objects = UserAccountManager()

    REQUIRED_FIELDS = ['groups_id', 'email']
    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'api_user'
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')


class Experience(BaseModel):
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)
    to_date = models.BooleanField(default=False)
    company_name = models.CharField(max_length=100, null=False, blank=False)
    position = models.CharField(max_length=100, null=False, blank=False)
    user = models.ForeignKey(User, related_name='experiences',  on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Опыт работы')
        verbose_name_plural = _('Опыт работ')
