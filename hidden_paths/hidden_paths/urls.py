"""
URL configuration for hidden_paths project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from tours import views as views_tours
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_tours.principal, name="Principal"),
    path('Tours/', views.tours, name="Tours"),
    path('Conocenos/', views.Conocenos, name="Conocenos"),
    path('Login/', views.Login, name="LOGIN"),
    path('CrearCuenta/', views.CrearCuenta,  name="Registrarse"),
    path('Agendar/', views.Agendar, name='Agendar'),
    path('payment/', views.payment, name='Payment'), 
    path('tours/', views.tours_list, name='Tours'),
    path('add_review/', views.add_review, name='add_review'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
