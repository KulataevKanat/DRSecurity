from django.urls import path

from api.views import ExperienceViews

urlpatterns = [
    path("create_experience/", ExperienceViews.CreateExperienceView.as_view()),
    path("delete_experience_by_id/<int:pk>/", ExperienceViews.DeleteExperienceByIdView.as_view()),
    path("update_experience_by_id/<int:pk>/", ExperienceViews.UpdateExperienceByIdView.as_view()),
    path("find_all_experiences/", ExperienceViews.GetExperienceView.as_view()),
    path("find_experience_by_id/<int:pk>/", ExperienceViews.FindExperienceByIdView.as_view()),
]
