from api.models import Experience
from rest_framework import generics

from api.serializers import ExperienceSerializers


class CreateExperienceView(generics.CreateAPIView):
    """Добавление опыта работы"""

    serializer_class = ExperienceSerializers.AllExperienceSerializer


class DeleteExperienceByIdView(generics.DestroyAPIView):
    """Удаление опыта работы по идентификации"""

    queryset = Experience.objects.all()


class UpdateExperienceByIdView(generics.UpdateAPIView):
    """Обновление опыта работы по идентификации"""

    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializers.AllExperienceSerializer


class GetExperienceView(generics.ListAPIView):
    """Вывод опыта работ"""

    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializers.AllExperienceSerializer


class FindExperienceByIdView(generics.RetrieveAPIView):
    """Поиск опыта работы по идентификации"""

    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializers.AllExperienceSerializer
