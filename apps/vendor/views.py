# Importaciones de módulos Django y modelos necesarios
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from django.shortcuts import redirect, render
from .models import Vendor
from apps.product.models import Product
from .forms import ProductForm

# Vista para el registro de nuevos vendedores
def become_vendor(request):
    if request.method=='POST': # Procesa el formulario de registro si la solicitud es de tipo POST
        
        form=UserCreationForm(request.POST)
        
        if form.is_valid(): # Registra al usuario, inicia sesión y crea un vendedor asociado al usuario
            user=form.save()
            
            login(request,user)
            
            vendor= Vendor.objects.create(name=user.username,created_by=user)
            
            
            return redirect('frontpage') # Redirige a la página principal
         
    else:
        form=UserCreationForm() # Crea un formulario vacío para mostrar al usuario
    
    return render(request,'vendor/become_vendor.html',{'form':form})

# Vista de administración para vendedores autenticados
@login_required
def vendor_admin(request):
    
    vendor=request.user.vendor # Obtenemos el vendedor asociado al usuario autenticado

     # Obtenemos todos los productos y pedidos del vendedor
    products=vendor.products.all()
    orders=vendor.orders.all()
    
    
    for order in orders:
        # Inicializa variables para cálculos relacionados con pedidos
        order.vendor_amount=0
        order.vendor_paid_amount=0
        order.fully_paid=True
    
        for item in order.items.all():
              # Verifica si el elemento pertenece al vendedor actual
            if item.vendor == request.user.vendor:
                # Calcula el monto total del pedido y el monto total pagado
                if item.vendor_paid:
                    order.vendoounr_paid_amt +=item.get_total_price()
                else:
                    order.vendor_amount += item.get_total_price()
                    order.fully_paid=False
                
       # Renderiza la página de administración con el contexto
    return render(request,'vendor/vendor_admin.html',{'vendor':vendor,'products':products,'orders':orders})

# Vista para agregar productos, accesible solo para usuarios autenticados
@login_required
def add_product(request):
    if request.method=='POST': # Procesa el formulario de producto si la solicitud es de tipo POST
        form =ProductForm(request.POST,request.FILES)
        
        if form.is_valid():
            
            product =form.save(commit=False) # Guarda el producto sin grabarlo en la base de datos de inmediato
            product.vendor=request.user.vendor # Asigna al producto el vendedor actual y genera un "slug" a partir del título
            product.slig=slugify(product.title)
            product.save() # Guarda el producto definitivamente en la base de datos
            
            return redirect('vendor_admin') # Redirige a la página de administración
        
    else:
        form=ProductForm() # Crea un formulario vacío para mostrar al usuario
    
    # Renderiza la página de agregar productos con el formulario como contexto
    return render(request,'vendor/add_product.html',{'form': form})