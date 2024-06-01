from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.status import HTTP_400_BAD_REQUEST,HTTP_201_CREATED
from django.http import JsonResponse
from django.middleware.csrf import get_token
from json import loads as jsonLoads
from rest_framework.response import Response
from .models import Asset,Service,Sale,Site,CurrencyType,Kind,Product
from .serializers import AssetFilter,AssetSerializer,ServiceFilter,ServiceSerializer,SaleSerializer,SaleFilter,SiteSerializer,CurrencyTypeSerializer,TypeSerializer,ProductFilter,ProductSerializer,UserFilter,UserSerializer
class TypeViewSet(ModelViewSet):
    queryset = Kind.objects.all();serializer_class = TypeSerializer 
class ProductViewSet(ModelViewSet):
    queryset=Product.objects.all(); serializer_class=ProductSerializer;filterset_class=ProductFilter
    def get_queryset(self):
        queryset= super().get_queryset();kind = self.request.query_params.get('kind')#filter by kind
        if kind:queryset = queryset.filter(kind=kind)
        search=self.request.query_params.get('search', None)
        if search is not None:queryset=queryset.filter(product__icontains=search)|queryset.filter(description__icontains=search)
        return queryset  
#class SaleViewSet(ModelViewSet):queryset=Sale.objects.all();serializer_class=SaleSerializer
class SiteViewSet(ModelViewSet):queryset=Site.objects.all();serializer_class=SiteSerializer
class CurrencyTypeViewSet(ModelViewSet):queryset=CurrencyType.objects.all();serializer_class=CurrencyTypeSerializer
class ServiceViewSet(ModelViewSet):
    queryset=Service.objects.all();serializer_class=ServiceSerializer;filterset_class = ServiceFilter
    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.query_params.get('title')
        if title:queryset = queryset.filter(title__exact=title)
        return queryset
class UserViewSet(ModelViewSet):
    queryset=User.objects.all();serializer_class=UserSerializer;filterset_class=UserFilter
    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.request.query_params.get('username')
        if username:queryset = queryset.filter(username__exact=username)
        return queryset
class AssetViewSet(ModelViewSet):
    queryset=Asset.objects.all();serializer_class=AssetSerializer;filter_backends=[DjangoFilterBackend];filterset_class=AssetFilter;permission_classes=[IsAuthenticated]
    def get_queryset(self):
        user=self.request.user
        if user:
            return Asset.objects.filter(client=user)
        else:
            return []
    def post(self,request):
        if request.method == 'POST':
            csrf_token=get_token(request)
            if request.POST.get('csrfmiddlewaretoken') == csrf_token:
                jd=jsonLoads(request.body)
                Asset.objects.create(video=jd['video'],title=jd['title'],client=jd['client'])
                data={'message':'Done!'}
                return JsonResponse(data)
            return JsonResponse({'error':'Method not allowed or invalid token'},status=400)
class SaleViewSet(ModelViewSet):
    queryset=Sale.objects.all();serializer_class=SaleSerializer;filter_backends=[DjangoFilterBackend];filterset_class=SaleFilter#;permission_classes=[IsAuthenticated]
    def get_queryset(self):
        user=self.request.user
        if user:
            return Sale.objects.filter(client=user)
        else:
            return []
class SaleCreateView(APIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    #permission_classes = [IsAuthenticated]
    def post(self, request):
        product_name = request.data.get('product')
        amount = request.data.get('amount')
        discount = request.data.get('discount', 0)

        if not product_name or not amount:
            return Response({'error': 'Product and amount are required'}, status=HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(product=product_name)
        except Product.DoesNotExist:
            return Response({'error': 'Product does not exist'}, status=HTTP_400_BAD_REQUEST)

        client = request.user

        try:
            sale = Sale.objects.create(product=product, client=client, amount=amount, discount=discount)
            return Response({'message': 'Sale created successfully'}, status=HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({"error": "Username and password are required"}, status=HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password)
        return Response({"message": "User created successfully"}, status=HTTP_201_CREATED)