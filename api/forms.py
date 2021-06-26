from django import forms
from django.forms import ModelForm
from .models import Person
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person 
        fields = [
            'name','phone','email', 'continent', 'country','district',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','required':''}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            # 'continent': forms.TextInput(attrs={'class':'form-control','required':''}),
            'continent': forms.Select(attrs={'class' : 'select2 form-control'}),
            'country': forms.Select(attrs={'class' : 'select2 form-control'}),
            'district': forms.TextInput(attrs={'class':'form-control','required':''}),
            
            # 'city': forms.TextInput(attrs={'class':'form-control','required':''}),
            # 'division': forms.TextInput(attrs={'class':'form-control','required':''}),
            # 'state': forms.TextInput(attrs={'class':'form-control','required':''}),
            # 'country': forms.TextInput(attrs={'class':'form-control','required':''}),
            # 'shop_city': forms.Select(attrs={'class' : 'select2 form-control'}),
            
        }
    
