import os
import django
from django.contrib.auth.models import Group

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dr_security.settings')

django.setup()

GROUPS = ['admin', 'user']
MODELS = ['user']

for group in GROUPS:
    new_group, created = Group.objects.get_or_create(name=group)
