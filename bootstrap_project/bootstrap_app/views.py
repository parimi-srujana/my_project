from django.shortcuts import render
from .models import Product
def product_list(request):
    if not Product.objects.exists():
        Product.objects.create(name='ASUS Vivobook', description='Lightweight laptop with high performance', price='2200')
        Product.objects.create(name='REAL ME', description='Innovative foldable screen smartphone', price='1400')
        Product.objects.create(name='REALME PODS', description='High-quality sound with long battery life', price='180')
        Product.objects.create(name='BOAT', description='Monitor health metrics and activities', price='150')
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})