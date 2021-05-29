from rest_framework import viewsets
from .serializers import ProductSerializer, SkuSerializer, BatchSerializer
from .models import Product, Sku, Batch


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SkuViewset(viewsets.ModelViewSet):
    queryset = Sku.objects.all()
    serializer_class = SkuSerializer


class BatchViewset(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
