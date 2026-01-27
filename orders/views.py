from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404

from customers.models import Customer
from products.models import Product
from .models import Order, OrderItem


@login_required
def order_list(request):
    orders = Order.objects.all().order_by('-order_date')
    return render(request, 'orders/order_list.html', {'orders': orders})


@login_required
@transaction.atomic
def order_create(request):
    customers = Customer.objects.all()
    products = Product.objects.all()

    # 🔒 Backend safety: no customer → no order
    if not customers.exists():
        messages.error(request, "Please create a customer before creating an order.")
        return redirect('customer_add')

    if not products.exists():
        messages.error(request, "Please add at least one product before creating an order.")
        return redirect('product_add')
    
    if request.method == 'POST':
        customer_id = request.POST.get('customer')
        product_ids = request.POST.getlist('product')

        # 🔒 No product selected
        if not product_ids:
            messages.error(request, "Please select at least one product.")
            return render(request, 'orders/order_create.html', {
                'customers': customers,
                'products': products,
                'has_customers': True
            })

        customer = get_object_or_404(Customer, id=customer_id)

        # 🔍 Stock pre-check
        for pid in product_ids:
            product = get_object_or_404(Product, id=pid)
            qty = int(request.POST.get(f'quantity_{pid}', 1))

            if qty < 1:
                messages.error(request, "Quantity must be at least 1.")
                return redirect('order_create')

            if product.stock < qty:
                messages.error(
                    request,
                    f"Insufficient stock for product: {product.name}"
                )
                return render(request, 'orders/order_create.html', {
                    'customers': customers,
                    'products': products,
                    'has_customers': True
                })

        # ✅ Create order AFTER validation
        order = Order.objects.create(customer=customer)

        total = 0
        for pid in product_ids:
            product = Product.objects.get(id=pid)
            qty = int(request.POST.get(f'quantity_{pid}', 1))

            subtotal = product.price * qty
            total += subtotal

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=qty,
                price=product.price
            )

            product.stock -= qty
            product.save()

        order.total_amount = total
        order.save()

        messages.success(request, "Order created successfully")
        return redirect('order_list')

    return render(request, 'orders/order_create.html', {
        'customers': customers,
        'products': products,
        'has_customers': True,
        'has_products': True
    })
