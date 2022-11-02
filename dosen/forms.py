from django.forms import ModelForm
from django import forms
from dosen.models import Dosen

class FormDosen(forms.ModelForm):
    class Meta:
        model = Dosen
        exclude = ['foto']

        widgets = {
            'no' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Nomor'}),
            'nip' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'NIP'}),
            'nama' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama'}),
            'jabatan' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Jabatan'}),
            'fakultas' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Fakultas'}),
            'email' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}),
        }