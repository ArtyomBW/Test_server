from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, UserQRcodeCreateAPIView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),

]

# path('api-QR', UserQRcodeCreateAPIView.as_view(), name='api-QR'),





