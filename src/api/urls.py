from django.urls import path, include

from api.endpoints import ExperienceEndpoints, GroupEndpoints, UserEndpoints

urlpatterns = [
    path('experience/', include(ExperienceEndpoints)),
    path('group/', include(GroupEndpoints)),
    path('user/', include(UserEndpoints)),
]
