from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from django.shortcuts import redirect, render

from .models import Vendor
from apps.product.models import Product


from .forms import ProductForm
# Create your views here.

def become_vendor(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        
        if form.is_valid():
            user=form.save()
            
            login(request,user)
            
            vendor= Vendor.objects.create(name=user.username,created_by=user)
            
            
            return redirect('frontpage')
        
    else:
        form=UserCreationForm()
    
    return render(request,'vendor/become_vendor.html',{'form':form})

@login_required
def vendor_admin(request):
    vendor=request.user.vendor
    products=vendor.products.all()
    orders=vendor.orders.all()
    
    
    for order in orders:
        order.vendor_amount=0
        order.vendor_paid_amount=0
        order.fully_paid=True
    
        for item in order.items.all():
            if item.vendor == request.user.vendor:
                if item.vendor_paid:
                    order.vendor_paid_amount +=item.get_total_price()
                else:
                    order.vendor_amount += item.get_total_price()
                    order.fully_paid=False
                
    
    return render(request,'vendor/vendor_admin.html',{'vendor':vendor,'products':products,'orders':orders})


@login_required
def add_product(request):
    if request.method=='POST':
        form =ProductForm(request.POST,request.FILES)
        
        if form.is_valid():
            product =form.save(commit=False)
            product.vendor=request.user.vendor
            product.slig=slugify(product.title)
            product.save()
            
            return redirect('vendor_admin')
        
    else:
        form=ProductForm()
    
    return render(request,'vendor/add_product.html',{'form': form})