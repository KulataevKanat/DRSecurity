from rest_framework import serializers

from office.models import User, Table


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password',
                  'first_name', 'last_name', 'groups', 'is_active']


class TableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'
