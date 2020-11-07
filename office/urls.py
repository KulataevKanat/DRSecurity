from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from office import views

urlpatterns = [
    url('login/', views.login_view, name='login'),
    url('refresh/', views.refresh_token_view, name='refresh'),
    url('api-auth/', include('rest_framework.urls', namespace='rest_employment'))
]
