from django import forms
from django.forms import ModelForm
from .models import Person
from .fields import ListTextWidget
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person 
        fields = [
            # 'name','phone','email', 'continent', 'country'
            'name','phone','email', 'continent', 'country','district'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','required':''}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            # 'continent': forms.TextInput(attrs={'class':'form-control','required':''}),
            'continent': forms.Select(attrs={'class' : 'select2 form-control'}),
            # 'country': forms.Select(attrs={'class' : 'select2 form-control'}),
            # 'district': forms.Select(attrs={'class' : 'select2 form-control'}),
            # 'district': forms.TextInput(attrs={'class':'form-control','required':''}),
            
            # 'city': forms.TextInput(attrs={'class':'form-control','required':''}),
            # 'division': forms.TextInput(attrs={'class':'form-control','required':''}),
            # 'state': forms.TextInput(attrs={'class':'form-control','required':''}),
            # 'country': forms.TextInput(attrs={'class':'form-control','required':''}),
            # 'shop_city': forms.Select(attrs={'class' : 'select2 form-control'}),
            
        }
    def __init__(self, *args, **kwargs):
        _district_set = kwargs.pop('district_set', None)
        _country_set = kwargs.pop('country_set', None)
        _continent_set = kwargs.pop('continent_set', None)
        super(PersonForm, self).__init__(*args, **kwargs) 
        self.fields['district'].widget = ListTextWidget(data_list=_district_set,name='district_set')
        self.fields['country'].widget = ListTextWidget(data_list=_country_set,name='country_set')
        self.fields['continent'].widget = ListTextWidget(data_list=_continent_set,name='continent_set')


    
