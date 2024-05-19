from rest_framework import serializers

from api.models import Table


class AllTableSerializer(serializers.ModelSerializer):
    """Добавление, Изменение, Вывод столов"""

    class Meta:
        model = Table
        fields = [
            'id',
            'name',
            'created',
            'updated',
        ]
