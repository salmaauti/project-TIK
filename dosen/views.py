from django.shortcuts import render, redirect
from dosen.models import Dosen
from dosen.forms import FormDosen
from django.contrib import messages
# Create your views here.
def hapus_dosen(request, id_dosen):
    dosen = Dosen.objects.filter(id=id_dosen)
    dosen.delete()
    if request.method == "POST":
        dosen.hapus()

    return redirect('dosen')


def ubah_dosen(request, id_dosen):
    dosen = Dosen.objects.get(id=id_dosen)
    template = 'ubah-dosen.html'
    if request.POST:
        form = FormDosen(request.POST, instance=dosen)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui") 
            return redirect('ubah_dosen', id_mdosen=id_dosen)

    else:
        form = FormDosen(instance=dosen)
        context = {
            'form': form,
            'dosen': dosen,
        }
        return render(request, template, context)

def dosen(request):
    context = {
        'lecturer': Dosen.objects.all()
        
    }
    return render(request,"dosen.html", context)

def tambah_dosen(request):
    if request.POST:
        form = FormDosen(request.POST)
        if form.is_valid():
            form.save()
            form = FormDosen()
            pesan = "Data berhasil disimpan"
            context = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-dosen.html', context)
    
    else:
        form = FormDosen()
    
        context = {
            'form': form,

        }
    return render(request, 'tambah-dosen.html', context)