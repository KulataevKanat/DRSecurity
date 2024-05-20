from rest_framework import serializers
from api.models import Experience


class AllExperienceSerializer(serializers.ModelSerializer):
    """Добавление, Изменение и Вывод опыта работ"""

    class Meta:
        model = Experience
        fields = [
            'start_date',
            'end_date',
            'to_date',
            'company_name',
            'position',
            'user',
        ]
