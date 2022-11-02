from django.forms import ModelForm
from django import forms
from tendik.models import Tendik

class FormTendik(forms.ModelForm):
    class Meta:
        model = Tendik
        exclude = '__all__'

        widgets = {
            'no' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Nomor'}),
            'nip' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'NIP'}),
            'nama' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama'}),
            'jabatan' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Jabatan'}),
        }