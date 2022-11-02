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
from django.conf.urls.static import static
from django.conf import settings
from faperta.views import faperta
from feb.views import feb
from fh.views import fh
from fisip.views import fisip
from fk.views import fk
from fkip.views import fkip
from ft.views import ft
from pascasarjana.views import pascasarjana
from universitas.views import universitas
from profil.views import profil
from dosen.views import dosen
from dosen.views import tambah_dosen
from dosen.views import ubah_dosen
from dosen.views import hapus_dosen
from mahasiswa.views import mahasiswa
from mahasiswa.views import tambah_mahasiswa
from mahasiswa.views import ubah_mahasiswa
from mahasiswa.views import hapus_mahasiswa
from tendik.views import tendik
from tendik.views import tambah_tendik
from tendik.views import ubah_tendik
from tendik.views import hapus_tendik


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
    path('universitas/', universitas, name="universitas"),
    path('profil/', profil, name="profil"),
    path('dosen/', dosen, name="dosen"),
    path('tambah-dosen/', tambah_dosen, name="tambah_dosen"),
    path('dosen/ubah/<int:id_dosen>', ubah_dosen, name="ubah_dosen"),
    path('dosen/hapus/<int:id_dosen>', hapus_dosen, name="hapus_dosen"),
    path('mahasiswa/', mahasiswa, name="mahasiswa"),
    path('tambah-mahasiswa/', tambah_mahasiswa, name="tambah_mahasiswa"),
    path('mahasiswa/ubah/<int:id_mahasiswa>', ubah_mahasiswa, name="ubah_mahasiswa"),
    path('mahasiswa/hapus/<int:id_mahasiswa>', hapus_mahasiswa, name="hapus_mahasiswa"),
    path('tendik/', tendik, name="tendik"),
    path('tambah-tendik/', tambah_tendik, name="tambah_tendik"),
    path('tendik/ubah/<int:id_tendik>', ubah_tendik, name="ubah_tendik"),
    path('tendik/hapus/<int:id_tendik>', hapus_tendik, name="hapus_tendik"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)