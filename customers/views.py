from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomerCreationForm, UserUpdateForm , CustomerUpdateForm, AddressCreationForm
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from orders.models import Order
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        customer_form = CustomerCreationForm(request.POST)
        address_form = AddressCreationForm(request.POST)
        if user_form.is_valid() and customer_form.is_valid() and address_form.is_valid():
            user = user_form.save()
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()
            address = address_form.save(commit=False)
            address.customer = customer
            address.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        user_form = UserCreationForm()
        customer_form = CustomerCreationForm()
        address_form = AddressCreationForm()
    return render(request, 'customers/signup.html', {'user_form': user_form,'customer_form': customer_form,'address_form':address_form})

@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        customer_form = CustomerUpdateForm(request.POST, instance=request.user.customer_profile)
        address_form = AddressCreationForm(request.POST, instance=request.user.customer_profile.address_set.last())
        if user_form.is_valid() and customer_form.is_valid() and address_form.is_valid():
            user_form.save()
            customer_form.save()
            address_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        customer_form = CustomerUpdateForm(instance=request.user.customer_profile)
        address_form = AddressCreationForm(instance=request.user.customer_profile.address_set.last())
    context = {
        'title': 'your profile',
        'user_form':user_form,
        'customer_form':customer_form,
        'address_form': address_form
    }
    return render(request,'customers/profile.html',context)



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home-page')

    else:
        form = AuthenticationForm()

    context = {
        'form': form,
        'title' : 'login page'
    }
    return render(request,'customers/login.html', context)



class OrderListView(LoginRequiredMixin,ListView):
    model = Order
    template_name = 'customers/order-list.html'
    
    def get_queryset(self):
        return Order.objects.filter(customer__user=self.request.user).order_by("-id")


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'customers/order-detail.html'
    