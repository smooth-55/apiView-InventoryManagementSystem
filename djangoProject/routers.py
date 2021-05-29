from rest_framework import routers
from myApp.viewsets import ProductViewset, SkuViewset, BatchViewset

router = routers.DefaultRouter()
router.register('product-api', ProductViewset)
router.register('sku-api', SkuViewset)
router.register('batch-api', BatchViewset)
