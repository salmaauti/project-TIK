from django.shortcuts import render, redirect
from mahasiswa.models import Mahasiswa
from mahasiswa.forms import FormMahasiswa
from django.contrib import messages
# Create your views here.

def hapus_mahasiswa(request, id_mahasiswa):
    mahasiswa = Mahasiswa.objects.filter(id=id_mahasiswa)
    mahasiswa.delete()
    if request.method == "POST":
        mahasiswa.hapus()

    return redirect('mahasiswa')


def ubah_mahasiswa(request, id_mahasiswa):
    mahasiswa = Mahasiswa.objects.get(id=id_mahasiswa)
    template = 'ubah-mahasiswa.html'
    if request.POST:
        form = FormMahasiswa(request.POST, instance=mahasiswa)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui") 
            return redirect('ubah_mahasiswa', id_mahasiswa=id_mahasiswa)

    else:
        form = FormMahasiswa(instance=mahasiswa)
        context = {
            'form': form,
            'mahasiswa': mahasiswa,
        }
        return render(request, template, context)

def mahasiswa(request):
    context = {
        'student': Mahasiswa.objects.all()
        
    }
    return render(request,"mahasiswa.html", context)

def tambah_mahasiswa(request):
    if request.POST:
        form = FormMahasiswa(request.POST)
        if form.is_valid():
            form.save()
            form = FormMahasiswa()
            pesan = "Data berhasil disimpan"
            context = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-mahasiswa.html', context)
    
    else:
        form = FormMahasiswa()
    
        context = {
            'form': form,

        }
    return render(request, 'tambah-mahasiswa.html', context)