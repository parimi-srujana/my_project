from django.shortcuts import render, redirect
from django.http import HttpResponse
import json

def home(request):
    return render(request, 'home.html')  # Renders homepage template

def add_to_cart(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_cost = float(request.POST.get('item_cost', 0))

        cart = json.loads(request.COOKIES.get('cart', '[]'))  # Get cart from cookies
        cart.append({'name': item_name, 'cost': item_cost})  # Add item to cart

        response = redirect('view_cart')
        response.set_cookie('cart', json.dumps(cart))  # Store cart in cookies
        return response

def view_cart(request):
    cart = json.loads(request.COOKIES.get('cart', '[]'))  # Retrieve cart from cookies
    total_cost = sum(item['cost'] for item in cart)  # Calculate total cost

    return render(request, 'cart.html', {'cart': cart, 'total_cost': total_cost})

def clear_cart(request):
    response = redirect('view_cart')
    response.delete_cookie('cart')  # Remove cart cookie
    return response

