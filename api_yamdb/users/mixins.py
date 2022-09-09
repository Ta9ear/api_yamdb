from rest_framework import mixins, viewsets


class RetrieveUpdateViewSet(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    """Вьюсет, выдающий только один элемент, который можно обновить."""
    pass
