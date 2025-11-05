from rest_framework import viewsets

from djshop.apps.catalog.serializers.admin import CategoryTreeSerializer
from djshop.apps.catalog.models import Category
from djshop.apps.catalog.serializers.admin import CreateCategoryNodeSerializer


class CategoryViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        if self.action == "list":
            return Category.objects.filter(depth=1)
        else:
            return Category.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return CategoryTreeSerializer
        else:
            return CreateCategoryNodeSerializer