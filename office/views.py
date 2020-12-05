import jwt
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from rest_framework import exceptions, viewsets
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from DrJwt import settings
from office.authentication import SafeJWTAuthentication
from office.models import Table
from office.permissions.permission import ROLE_ADMIN, ROLE_USER
from office.serializers import UserSerializer, TableSerializer
from office.provider import generate_access_token, generate_refresh_token


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    authentication_classes = [SafeJWTAuthentication]

    def get_permissions(self):
        permission_class = []
        if self.action == 'create':
            permission_class = [ROLE_ADMIN]
        elif self.action == 'list':
            permission_class = [ROLE_USER]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_class = [ROLE_ADMIN]
        elif self.action == 'destroy':
            permission_class = [ROLE_ADMIN]
        return [permission() for permission in permission_class]


@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def access_token_view(request):
    User = get_user_model()
    username = request.data.get('username')
    password = request.data.get('password')
    response = Response()

    if (username is None) or (password is None):
        raise exceptions.AuthenticationFailed('username and password required')

    user = User.objects.filter(username=username).first()

    if user is None:
        raise exceptions.AuthenticationFailed('user not found')

    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('wrong password')

    serialized_user = UserSerializer(user).data

    access_token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)

    response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
    response.data = {
        'access_token': access_token,
        'user': serialized_user,
    }

    return response


@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_protect
def refresh_token_view(request):
    User = get_user_model()
    refresh_token = request.COOKIES.get('refresh_token')

    if refresh_token is None:
        raise exceptions.AuthenticationFailed('Authentication credentials were not provided.')
    try:
        payload = jwt.decode(refresh_token, settings.REFRESH_TOKEN_SECRET, algorithms=['HS256'])

    except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed('expired refresh token, please login again.')

    user = User.objects.filter(id=payload.get('user_id')).first()

    if user is None:
        raise exceptions.AuthenticationFailed('User not found')

    if not user.is_active:
        raise exceptions.AuthenticationFailed('user is inactive')

    access_token = generate_access_token(user)

    return Response({'access_token': access_token})
