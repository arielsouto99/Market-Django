"""
Proyecto Final
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.home.urls')),
    # users app
    path('', include('applications.users.urls')),
    # producto app
    path('', include('applications.producto.urls')),
    # venta app
    path('', include('applications.venta.urls')),
    # caja app
    path('', include('applications.caja.urls')),
]
