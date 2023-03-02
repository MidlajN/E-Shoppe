from django.shortcuts import render, redirect
from .forms import SellerCreationForm, BuyerCreationForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from E_App.models import Product


# Create your views here.
def base_acc(request):
    form_seller = SellerCreationForm()
    form_buyer = BuyerCreationForm()
    context = {
        'form_seller': form_seller,
        'form_buyer': form_buyer
    }
    return render(request, 'register.html', context=context)

def buyer_reg(request):
    if request.method == 'POST':
        form_buyer = BuyerCreationForm(request.POST)
        if form_buyer.is_valid():
            form_buyer.save()
            return redirect('E_App:AllProdCat')
        else:
            form_buyer = BuyerCreationForm()
            messages.info(request, 'Invalid Input')

        return redirect('E_User:user')
    

def seller_reg(request):
    if request.method == 'POST':
        form_seller = SellerCreationForm(request.POST)
        if form_seller.is_valid():
            form_seller.save()
            return redirect('E_App:AllProdCat')
        else:
            form_seller = SellerCreationForm()
            print(form_seller.errors, form_seller.non_field_errors)
            messages.info(request, 'Invalid Input')
    
        return redirect('E_User:Register')
    

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.info(request, 'Welcome {username}.')
                return redirect('E_App:AllProdCat')
            else:
                messages.info(request, 'Invalid Credential')
                return redirect('E_User:Login')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'login_form': form})

def logout(request):
    auth.logout(request)
    return redirect('E_App:AllProdCat')


def dashboard(request):
    
    if request.user.is_seller == True:
        products = Product.objects.all().filter(seller=request.user)
        
    else:
        messages.info(request, 'User is Buyer')
        
    
    return render(request, 'dashboard.html', {'products': products})