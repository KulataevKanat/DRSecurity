from django.urls import path

from api.views import GroupViews

urlpatterns = [
    path("create_group/", GroupViews.CreateGroupView.as_view()),
    path("delete_group_by_id/<int:pk>/", GroupViews.DeleteGroupByIdView.as_view()),
    path("update_group_by_id/<int:pk>/", GroupViews.UpdateGroupByIdView.as_view()),
    path("find_all_groups/", GroupViews.GetGroupView.as_view()),
    path("find_group_by_id/<int:pk>/", GroupViews.FindGroupByIdView.as_view()),
]
