"""untirta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from faperta.views import faperta
from feb.views import feb
from fh.views import fh
from fisip.views import fisip
from fk.views import fk
from fkip.views import fkip
from ft.views import ft
from pascasarjana.views import pascasarjana


urlpatterns = [
    path('admin/', admin.site.urls),
    path('faperta/', faperta, name="faperta"),
    path('feb/', feb, name="feb"),
    path('fh/', fh, name="fh"),
    path('fisip/', fisip, name="fisip"),
    path('fk/', fk, name="fk"),
    path('fkip/', fkip, name="fkip"),
    path('ft/', ft, name="ft"),
    path('pascasarjana/', pascasarjana, name="pascasarjana"),

]
