from django.contrib import admin
from django.urls import path, include
from api import urls as office_urls
from dr_security.swagger import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(office_urls)),
]

urlpatterns += doc_urls
