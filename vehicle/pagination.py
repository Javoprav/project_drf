from rest_framework.pagination import PageNumberPagination


class MaterialsPagination(PageNumberPagination):
    """Реализовать пагинацию для всех эндпоинтов, которые отвечают за вывод списка сущностей.
Описать класс пагинации.
Добавить класс пагинации к классу вывода списка сущностей."""
    page_size = 4  # Количество элементов на странице
    page_size_query_param = 'page_size'  # Параметр запроса для указания количества элементов на странице
    max_page_size = 100  # Максимальное количество элементов на странице

# class MyView(APIView):
#     pagination_class = MyPagination
#
#     def get(self, request):
#         queryset = MyModel.objects.all()
#         paginated_queryset = self.paginate_queryset(queryset)
#         serializer = MySerializer(paginated_queryset, many=True)
#         return self.get_paginated_response(serializer.data)


class MotoPagination(PageNumberPagination):
    page_size = 2  # Количество элементов на странице
    page_size_query_param = 'page_size'  # Параметр запроса для указания количества элементов на странице
    max_page_size = 50  # Максимальное количество элементов на странице
