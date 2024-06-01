from django.contrib.auth.models import User;
from rest_framework.serializers import ModelSerializer,CharField
from django_filters.rest_framework import FilterSet, CharFilter
from .models import Product, Kind, Sale,CurrencyType, Site, Service, Asset
class ProductFilter(FilterSet):
    kind=CharFilter(field_name='kind', lookup_expr='exact')
    product=CharFilter(method='filter_by_search', lookup_expr='icontains')
    def filter_by_search(self, queryset,value):return queryset.filter(product__icontains=value)|queryset.filter(description__icontains=value)
    class Meta:model=Product;fields={'kind':['exact'],'product':['icontains'],}
class ProductSerializer(ModelSerializer):
    class Meta: 
        model=Product
        fields=['product', 'kind', 'price', 'currency_type', 'image','description','stock']
class TypeSerializer(ModelSerializer):
    class Meta: model=Kind;fields=['kind']
class CurrencyTypeSerializer(ModelSerializer):
    class Meta: model=CurrencyType;fields=['currency_type']
class SiteSerializer(ModelSerializer):
    class Meta:model=Site;fields=['city']
class SaleFilter(FilterSet):
    class Meta:model=Sale;fields={'client':['exact']}
class SaleSerializer(ModelSerializer):
    product=ProductSerializer()
    class Meta:model=Sale;fields=['product','client','amount','discount','price_final'];depth=1
class ServiceFilter(FilterSet):
    title=CharFilter(field_name='title', lookup_expr='exact')
class ServiceSerializer(ModelSerializer):
    class Meta:model=Service;fields=['title','description','image','price','currency_types']#;filter_class=ServiceFilter
class UserFilter(FilterSet):
    class Meta:model=User; fields={'username':['exact']}
class UserSerializer(ModelSerializer):
    password=CharField(write_only=True,style={'input_type':'password'})
    class Meta:model=User;fields=['url','id','username','email','password','is_staff']#;filter_class=UserFilter
class AssetFilter(FilterSet):
    class Meta:model=Asset;fields={'client':['exact']}
class AssetSerializer(ModelSerializer):
    class Meta:model=Asset;fields=['video','title','client']