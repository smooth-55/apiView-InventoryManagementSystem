from .models import Product, Sku, Batch, Inventory
from .serializers import (
    ProductSerializer,
    BatchSerializer,
    SkuSerializer,
    InventorySerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  # HTTP status code


class ProductList(APIView):
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get(self, request, format=None):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get(self, request, pk, format=None):
        queryset = Product.objects.get(pk=pk)
        serializer = ProductSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = Product.objects.get(pk=pk)
        serializer = ProductSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        queryset = Product.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SkuList(APIView):
    def post(self, request):
        serializer = SkuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get(self, request, format=None):
        queryset = Sku.objects.all()
        serializer = SkuSerializer(queryset, many=True)
        return Response(serializer.data)


class SkuDetail(APIView):
    def get(self, request, pk, format=None):
        queryset = Sku.objects.get(pk=pk)
        serializer = SkuSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = Sku.objects.get(pk=pk)
        serializer = SkuSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        queryset = Sku.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BatchList(APIView):
    def post(self, request):
        serializer = BatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get(self, request):
        queryset = Batch.objects.all()
        serializer = BatchSerializer(queryset, many=True)
        return Response(serializer.data)


class BatchDetail(APIView):
    def get(self, pk, request, format=None):
        queryset = Batch.objects.get(pk=pk)
        serializer = BatchSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = Batch.objects.get(pk=pk)
        serializer = BatchSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        queryset = Batch.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InventoryList(APIView):
    def post(self, request, format=None):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get(self, request, format=None):
        queryset = Inventory.objects.all()
        serializer = InventorySerializer(queryset, many=True)
        return Response(serializer.data)


class InventoryDetail(APIView):
    def get(self, pk, request, format=None):
        queryset = Inventory.objects.get(pk=pk)
        serializer = InventorySerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = Inventory.objects.get(pk=pk)
        serializer = InventorySerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        queryset = Inventory.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)