from django.contrib.admin import site
from .models import Asset,CurrencyType,Kind,Product,Service,Sale,Site
#from rest_framework.authtoken.admin import TokenAdmin
site.register(Asset)
site.register(CurrencyType)
site.register(Kind)
site.register(Product)
site.register(Service)
site.register(Sale)
site.register(Site)
#TokenAdmin.raw_id_fields=['user']