from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from office import urls as office_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url('office/', include(office_urls)),

    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
