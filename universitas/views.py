from django.shortcuts import render
from universitas.models import Fakultas
# Create your views here.
def universitas(request):
    context = {
        'faculty': Fakultas.objects.all()
        
    }
    return render(request,'index.html', context)