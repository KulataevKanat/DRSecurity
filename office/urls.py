from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from office import views

router = DefaultRouter()
router.register('table', views.TableViewSet, basename='table')

urlpatterns = [
    url('table/', include(router.urls)),
    url('access/', views.access_token_view, name='access'),
    url('refresh/', views.refresh_token_view, name='refresh'),
]
