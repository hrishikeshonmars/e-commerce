from django.shortcuts import render,redirect
from ecomapp.models import Contact, Product, Orders, OrderUpdate
from django.contrib import messages
from math import ceil
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
import json
from django.core.paginator import Paginator

def index(request):
    category_products = []
    cat_prods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in cat_prods}
    
    for cat in cats:
        products = Product.objects.filter(category=cat)
        paginator = Paginator(products, 4)  # Paginate by 4 items per page
        page_number = request.GET.get('page')
        try:
            page_products = paginator.page(page_number)
        except PageNotAnInteger:
            page_products = paginator.page(1)
        except EmptyPage:
            page_products = paginator.page(paginator.num_pages)
        
        category_products.append({
            'category': cat,
            'products': page_products
        })

    return render(request, "index.html", {'category_products': category_products})


def my_view(request):
    products = Product.objects.all().order_by('name')  # Assuming 'name' is the field you want to order by
    paginator = Paginator(products, 4)  # Paginate by 4 items per page
    # Rest of your view logic

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        pnumber = request.POST.get("pnumber")
        my_query = Contact.objects.create(name=name, email=email, desc=desc, phonenumber=pnumber)
        messages.info(request, "We will get back to you soon..")
        return redirect("contact")

    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please login to proceed with checkout.")
        return redirect('/auth/login')
    
    if request.method == "POST":
        # Retrieve form data
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        
        # Create new order instance
        order = Orders.objects.create(items_json=items_json, name=name, amount=amount, email=email,
                                      address=address, city=city, state=state, zip_code=zip_code, phone=phone)
        
        # Create order update instance
        OrderUpdate.objects.create(order_id=order.id, update_desc="The order has been placed")
        
        # Redirect to thank you page
        return redirect("thank_you")

    # If it's a GET request, render the checkout page
    # Retrieve items from session or however you are storing them
    items = []  # Replace this with logic to retrieve items from session or database
    total_price = 0
    for item in items:
        total_price += item.price
    
    context = {
        'items': items,
        'total_price': total_price,
    }
    
    return render(request, "checkout.html", context)

