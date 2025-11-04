from rest_framework import viewsets

from djshop.apps.catalog.models import Category
from djshop.apps.catalog.serializers.admin import CreateCategoryNodeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CreateCategoryNodeSerializer