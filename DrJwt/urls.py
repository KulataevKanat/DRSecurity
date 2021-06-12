from django.contrib import admin
from django.urls import path, include
from office import urls as office_urls
from DrJwt.swagger import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('office/', include(office_urls)),
]

urlpatterns += doc_urls
