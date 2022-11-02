from django.shortcuts import render, redirect
from tendik.models import Tendik
from tendik.forms import FormTendik
from django.contrib import messages
# Create your views here.
def hapus_tendik(request, id_tendik):
    tendik = Tendik.objects.filter(id=id_tendik)
    tendik.delete()
    if request.method == "POST":
        tendik.hapus()

    return redirect('tendik')


def ubah_tendik(request, id_tendik):
    tendik = Tendik.objects.get(id=id_tendik)
    template = 'ubah-tendik.html'
    if request.POST:
        form = FormTendik(request.POST, instance=tendik)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui") 
            return redirect('ubah_tendik', id_mahasiswa=id_tendik)

    else:
        form = FormTendik(instance=tendik)
        context = {
            'form': form,
            'tendik': tendik,
        }
        return render(request, template, context)

def tendik(request):
    context = {
        'educator': Tendik.objects.all()
        
    }
    return render(request,"tendik.html", context)

def tambah_tendik(request):
    if request.POST:
        form = FormTendik(request.POST)
        if form.is_valid():
            form.save()
            form = FormTendik()
            pesan = "Data berhasil disimpan"
            context = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-tendik.html', context)
    
    else:
        form = FormTendik()
    
        context = {
            'form': form,

        }
    return render(request, 'tambah-tendik.html', context)