from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm
from django.core.paginator import Paginator


def dashboard(request):

    total_customers = Customer.objects.count()

    context = {
        "total_customers": total_customers
    }

    return render(request, "crm/dashboard.html", context)


def customers(request):

    search_query = request.GET.get('search')

    if search_query:
        customer_list = Customer.objects.filter(name__icontains=search_query)
    else:
        customer_list = Customer.objects.all()

    paginator = Paginator(customer_list, 5)  # 5 customers per page

    page_number = request.GET.get('page')

    customers = paginator.get_page(page_number)

    context = {
        "customers": customers
    }

    return render(request, "crm/customers.html", context)


def add_customer(request):

    if request.method == "POST":

        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('customers')

    else:
        form = CustomerForm()

    return render(request, "crm/add_customer.html", {"form": form})


def update_customer(request, pk):

    customer = Customer.objects.get(id=pk)

    if request.method == "POST":

        form = CustomerForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()
            return redirect('customers')

    else:
        form = CustomerForm(instance=customer)

    return render(request, "crm/update_customer.html", {"form": form})


def delete_customer(request, pk):

    customer = Customer.objects.get(id=pk)
    customer.delete()

    return redirect('customers')