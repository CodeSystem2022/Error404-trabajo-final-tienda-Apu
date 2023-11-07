from django.shortcuts import render


from apps.product.models import Product
# librerias para enviar correo
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import mi_formulario
# Create your views here.

def frontpage(request):
    newest_products=Product.objects.all()[0:8]
    return render(request, 'core/frontpage.html', {'newest_products': newest_products})


def contact(request):
    
    return render (request,'core/contact.html')

def enviar_correo(request):
    form = mi_formulario(request.POST)
    if request.method == 'POST':
        nombre = request.POST['nombre']
        correo = request.POST['correo']
        mensaje = request.POST['mensaje']
        
        
        # Formato del mensaje de correo
        mensaje = f'Información de contacto:\n\nLugar: {nombre}\n\n{mensaje}'

        # Enviar el correo
        send_mail('Información de contacto', mensaje, 'tienda_apu@hotmail.com', ['tienda_apu@hotmail.com'], fail_silently=False)

        # Redirigir a una página de confirmación
        return HttpResponseRedirect(reverse('envio'))
    else:
        print('EL MENSAJE A FALLADO')
    return render(request,'core/envio.html',{'envio':form})