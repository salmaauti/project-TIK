from django.contrib import admin
from universitas.models import Fakultas
# Register your models here.

class FakultasAdmin(admin.ModelAdmin):
    list_display = ['no','nama']
    search_fields = ['nama']
    

admin.site.register(Fakultas, FakultasAdmin)