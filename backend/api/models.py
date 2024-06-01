from django.db.models import Model,FileField,TextField, CASCADE,ImageField,CharField,ForeignKey, DecimalField,DateField,IntegerField;from decimal import Decimal;from django.core.validators import MinValueValidator;from django.contrib.auth.models import User;from django.utils.timezone import now
class Kind(Model):
    kind = CharField(unique=True, verbose_name='tipo',null=False, default='video')
    class Meta:
        verbose_name='tipo'
        verbose_name_plural='tipos'
    def __str__(self):return f'{self.kind}'
class CurrencyType(Model):
    currency_type = CharField(unique=True, null=False, default='euro', max_length=9)
    class Meta:
        verbose_name='tipo de divisa'
        verbose_name_plural='tipos de divisa'
    def __str__(self):return f'{self.currency_type}'
class Site(Model):
    city = CharField(unique=True, null=False, verbose_name='ciudad', default='Alcaucín')
    class Meta:
        verbose_name="Sede"
        verbose_name_plural="Sedes"
    def __str__(self):return f'{self.city}'
class Product(Model):
    product = CharField(verbose_name='producto',null=False, unique=True)
    image = ImageField(upload_to='products', default="camera.png", verbose_name='imagen')
    kind = ForeignKey(Kind, CASCADE, db_column='kind', to_field='kind', null=False)
    price = DecimalField(max_digits=10,decimal_places=2, null=False, validators=[MinValueValidator(0)], verbose_name='precio/ud')
    currency_type = ForeignKey(CurrencyType, CASCADE, db_column='currency_type', to_field='currency_type', null=False, default='euro')
    stock = IntegerField(null=False, verbose_name='stock', validators=[MinValueValidator(0)])
    description=TextField(verbose_name='descripción')
    class Meta:verbose_name="Producto";verbose_name_plural="Productos"
    def __str__(self):return f'{self.product}'
class Sale(Model):
    product = ForeignKey(Product, CASCADE, db_column='product', to_field='product', null=False, verbose_name="producto", default='camara')
    client = ForeignKey(User, CASCADE, db_column='username',verbose_name="cliente", null=False, default='pyCampaDB')
    amount = IntegerField(verbose_name="unidades",null=False, validators=[MinValueValidator(0)])
    discount = IntegerField(null=False, verbose_name='descuento', validators=[MinValueValidator(0)])
    price_final = DecimalField(verbose_name="precio final",max_digits=10, editable=False,decimal_places=2, null=False)
    date_sale = DateField(verbose_name='Fecha venta',default=now, editable=False)
    class Meta:
        verbose_name="Venta"
        verbose_name_plural="Ventas"
    def __str__(self):return f'{self.product}, {self.amount} uds. Importe: {self.price_final} {self.product.currency_type}'
    def save(self, *args, **kwargs):
        if self.product and self.discount is not None:discount_decimal = Decimal(self.discount);self.price_final = (self.product.price - self.product.price*(discount_decimal/100))*self.amount
        super().save(*args, **kwargs)
class Service(Model):
    title = CharField(max_length=8, null=False, verbose_name='Título', unique=True, default='')
    description = TextField(blank=True, null=True)
    image=ImageField(upload_to='services', default='key.png', verbose_name='Imagen')
    price=DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    currency_types = ForeignKey(CurrencyType, CASCADE, db_column='currency_types', to_field='currency_type')
    class Meta:
        managed =verbose_name='Servicio';verbose_name_plural='Servicios'
    def __str__(self):return f'{self.title}'
class Asset(Model):
    video=FileField(upload_to='assets', verbose_name='Video');title=IntegerField(verbose_name='title');client = ForeignKey(User, CASCADE, db_column='username',verbose_name="cliente", null=False, default='naruto')
    class Meta:verbose_name='Video'; verbose_name_plural='Videos'
    def __str__(self):return f'{self.video}'