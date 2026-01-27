from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from django.forms import ModelForm
from django.db import IntegrityError
from django.contrib import messages

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email']


@login_required
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})


@login_required
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Customer added successfully")
                return redirect('customer_list')
            except IntegrityError:
                messages.error(
                    request,
                    "Customer with this phone number or email already exists."
                )
    else:
        form = CustomerForm()

    return render(request, 'customers/customer_form.html', {'form': form})

@login_required
def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(request.POST or None, instance=customer)

    if form.is_valid():
        try:
            form.save()
            messages.success(request, "Customer updated successfully")
            return redirect('customer_list')
        except IntegrityError:
            messages.error(
                request,
                "Customer with this phone number or email already exists."
            )

    return render(request, 'customers/customer_form.html', {'form': form})


@login_required
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'customers/customer_confirm_delete.html', {'customer': customer})
