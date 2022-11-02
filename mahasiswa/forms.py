from django.forms import ModelForm
from django import forms
from mahasiswa.models import Mahasiswa

class FormMahasiswa(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        exclude = ['foto']

        widgets = {
            'no' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Nomor Absen'}),
            'nim' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'NIM'}),
            'nama' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama'}),
            'ttl' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tempat Tanggal Lahir'}),
            'email' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}),
        }

    
        
     