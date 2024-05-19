from django.urls import path
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny

from api.authentication import SafeJWTAuthentication
from api.permissions.permission import ROLE_ADMIN, UserPermissionsObj, ROLE_USER
from api.views import UserViews, GroupViews, TableViews

urlpatterns = [
    # USERS
    path("user/access_token/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.AccessToken)).as_view()),
    path("user/refresh_token/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([UserPermissionsObj])(UserViews.RefreshToken)).as_view()),
    path("user/registration/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.UserRegistrationView)).as_view()),
    path("user/create_super_user/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([ROLE_ADMIN])(UserViews.CreateSuperUserView)).as_view()),
    path("user/delete_user_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([UserPermissionsObj])(UserViews.DeleteUserByIdView)).as_view()),
    path("user/delete_all_users/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([ROLE_ADMIN])(UserViews.DeleteAllUsersView)).as_view()),
    path("user/update_user_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([UserPermissionsObj])(UserViews.UpdateUserView)).as_view()),
    path("user/find_all_users/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.GetUserView)).as_view()),
    path("user/find_user_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([ROLE_ADMIN])(UserViews.FindUserByIdView)).as_view()),

    # GROUPS
    path("group/create_group/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([ROLE_ADMIN])(GroupViews.CreateGroupView)).as_view()),
    path("group/delete_group_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([ROLE_ADMIN])(GroupViews.DeleteGroupByIdView)).as_view()),
    path("group/update_group_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([ROLE_ADMIN])(GroupViews.UpdateGroupByIdView)).as_view()),
    path("group/find_all_groups/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([ROLE_ADMIN])(GroupViews.GetGroupView)).as_view()),
    path("group/find_group_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([ROLE_ADMIN])(GroupViews.FindGroupByIdView)).as_view()),

    # TABLES
    path("table/create_table/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([ROLE_USER | ROLE_ADMIN])(TableViews.CreateTableView)).as_view()),
    path("table/delete_table_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([ROLE_USER | ROLE_ADMIN])(TableViews.DeleteTableByIdView)).as_view()),
    path("table/update_table_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([ROLE_USER | ROLE_ADMIN])(TableViews.UpdateTableByIdView)).as_view()),
    path("table/find_all_tables/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([ROLE_USER | ROLE_ADMIN])(TableViews.GetTableView)).as_view()),
    path("table/find_table_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([ROLE_USER | ROLE_ADMIN])(TableViews.FindTableByIdView)).as_view()),
]
