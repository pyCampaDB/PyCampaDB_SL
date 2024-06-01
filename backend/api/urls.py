from django.urls import path, include
from .views import RegisterView,ProductViewSet,AssetViewSet,TypeViewSet,CurrencyTypeViewSet,UserViewSet,SiteViewSet,ServiceViewSet,SaleViewSet,SaleCreateView
from rest_framework.routers import DefaultRouter
#from django.contrib.auth.models import User
router=DefaultRouter()
router.register(r'products',ProductViewSet)
router.register(r'types',TypeViewSet)
router.register(r'users',UserViewSet)
router.register(r'currency-types',CurrencyTypeViewSet)
router.register(r'assets',AssetViewSet)
router.register(r'sites',SiteViewSet)
router.register(r'services',ServiceViewSet)
router.register(r'sales', SaleViewSet)
urlpatterns = [
    path('api-auth/',include('rest_framework.urls'),name='rest_framework'),
    path('',include(router.urls)),
    path('register/',RegisterView.as_view(),name='register'),
    path('sale/new/',SaleCreateView.as_view(),name='new-sale' )
]
