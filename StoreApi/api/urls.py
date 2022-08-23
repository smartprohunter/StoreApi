from django.urls import path
from rest_framework.routers import DefaultRouter

from StoreApi.api.views import ProductViewSet, OrderViewSet, OrderStatsView

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'order', OrderViewSet, basename='order')

urls = [
    path('stats/', OrderStatsView.as_view(), name='stats'),

]

urlpatterns = router.urls + urls
