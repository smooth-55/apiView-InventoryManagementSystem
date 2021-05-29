from rest_framework import serializers
from .models import Product, Sku, Batch, Inventory


class ProductSerializer(serializers.ModelSerializer):
    sku = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "image",
            "label",
            "price",
            "brand",
            "description",
            "created_on",
            "sku",
        ]


class SkuSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Sku
        fields = [
            "id",
            "sku_code",
            "color",
            "size",
            "gender_category",
            "product",
            "created_on",
        ]


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ["id", "sku", "created_on"]


class InventorySerializer(serializers.ModelSerializer):
    inventory_sku = SkuSerializer(read_only=True)

    class Meta:
        model = Inventory
        fields = ["id", "remaining_stock", "inventory_sku", "created_on"]
