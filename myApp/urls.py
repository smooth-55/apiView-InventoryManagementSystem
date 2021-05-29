from django.urls import path
from . import apiView

urlpatterns = [
    path("products/", apiView.ProductList.as_view(), name="product-list"),
    path("products/<int:pk>/", apiView.ProductDetail.as_view(), name="product"),
    path("sku/", apiView.SkuList.as_view(), name="sku-list"),
    path("sku/<int:pk>/", apiView.SkuDetail.as_view(), name="sku"),
    path("batch/", apiView.BatchList.as_view(), name="batch-list"),
    path("batch/<int:pk>/", apiView.BatchDetail.as_view(), name="batch"),
    path("inventory/", apiView.InventoryList.as_view(), name="inventory-list"),
    path("inventory/<int:pk>/", apiView.InventoryDetail.as_view(), name="inventory"),
]
