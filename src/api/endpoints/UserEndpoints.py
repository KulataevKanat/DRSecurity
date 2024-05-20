from django.urls import path

from api.views import UserViews

urlpatterns = [
    path("access_token/", UserViews.AccessToken.as_view()),
    path("refresh_token/", UserViews.RefreshToken.as_view()),
    path("registration/", UserViews.UserRegistrationView.as_view()),
    path("create_super_user/", UserViews.CreateSuperUserView.as_view()),
    path("delete_user_by_id/<int:pk>/", UserViews.DeleteUserByIdView.as_view()),
    path("delete_all_users/", UserViews.DeleteAllUsersView.as_view()),
    path("find_all_users/", UserViews.GetUserView.as_view()),
    path("find_user_by_id/<int:pk>/", UserViews.FindUserByIdView.as_view()),
]
