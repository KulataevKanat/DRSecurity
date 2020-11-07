from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()
    DoesNotExist = models.Manager()

    class Meta:
        abstract = True
