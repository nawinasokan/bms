from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Sum

from customers.models import Customer
from products.models import Product
from orders.models import Order

@login_required
def dashboard_view(request):
    total_customers = Customer.objects.count()
    total_products = Product.objects.count()
    total_orders = Order.objects.count()
    total_revenue = Order.objects.aggregate(
        total=Sum('total_amount')
    )['total'] or 0

    context = {
        'total_customers': total_customers,
        'total_products': total_products,
        'total_orders': total_orders,
        'total_revenue': total_revenue,
    }

    return render(request, 'dashboard/dashboard.html', context)
