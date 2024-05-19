from rest_framework import generics

from api.models import Table
from api.serializers import TableSerializers


class CreateTableView(generics.CreateAPIView):
    """Добавление стола"""

    serializer_class = TableSerializers.AllTableSerializer


class DeleteTableByIdView(generics.DestroyAPIView):
    """Удаление стола по идентификации"""

    queryset = Table.objects.all()


class UpdateTableByIdView(generics.UpdateAPIView):
    """Обновление стола по идентификации"""

    queryset = Table.objects.all()
    serializer_class = TableSerializers.AllTableSerializer


class GetTableView(generics.ListAPIView):
    """Вывод столов"""

    queryset = Table.objects.all()
    serializer_class = TableSerializers.AllTableSerializer


class FindTableByIdView(generics.RetrieveAPIView):
    """Поиск стола по идентификации"""

    queryset = Table.objects.all()
    serializer_class = TableSerializers.AllTableSerializer
