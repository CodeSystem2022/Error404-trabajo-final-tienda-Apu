#
#

from django.urls import path

#
#

from .import views
#
#

urlpatterns = [
    path('',views.frontpage,name='frontpage'),
    path('contact/',views.contact,name='contact'),
    path('envio/',views.enviar_correo,name='envio'),
]
