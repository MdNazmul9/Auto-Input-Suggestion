from django import forms
from django.forms import ModelForm
from .models import Person
from .fields import ListTextWidget
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person 
        fields = [
            'name','phone','email', 'continent', 'country','state','division','district','city','road_or_streetNo', 'policestation','postoffice','zipcode','upozila_thana','municipality','union','word_no','village','mahalla','block','holdingNo','house'
        ]


        # widgets = {
        #     'name': forms.TextInput(attrs={'class':'form-control','required':''}),
        #     'phone': forms.TextInput(attrs={'class':'form-control'}),
        #     'email': forms.TextInput(attrs={'class':'form-control'}),
        #     # 'continent': forms.TextInput(attrs={'class':'form-control','required':''}),
        #     'continent': forms.Select(attrs={'class' : 'select2 form-control'}),
        #     # 'country': forms.Select(attrs={'class' : 'select2 form-control'}),
        #     # 'district': forms.Select(attrs={'class' : 'select2 form-control'}),
        #     # 'district': forms.TextInput(attrs={'class':'form-control','required':''}),
            
        #     # 'city': forms.TextInput(attrs={'class':'form-control','required':''}),
        #     # 'division': forms.TextInput(attrs={'class':'form-control','required':''}),
        #     # 'state': forms.TextInput(attrs={'class':'form-control','required':''}),
        #     # 'country': forms.TextInput(attrs={'class':'form-control','required':''}),
        #     # 'shop_city': forms.Select(attrs={'class' : 'select2 form-control'}),
            
        # }


    def __init__(self, *args, **kwargs):   
        _continent_set = kwargs.pop('continent_set', None)
        _country_set = kwargs.pop('country_set', None)
        _state_set = kwargs.pop('state_set', None)
        _division_set = kwargs.pop('division_set', None)
        _district_set = kwargs.pop('district_set', None)
        _city_set = kwargs.pop('city_set', None)
        _roadOrStreetNo_set = kwargs.pop('roadOrStreetNo_set', None)
        _policeStation_set = kwargs.pop('policeStation_set', None)
        _postOffice_set = kwargs.pop('postOffice_set', None)
        _zipCode_set = kwargs.pop('zipCode_set', None)
        _thanaUpozila_set= kwargs.pop('thanaUpozila_set', None)
        _municipality_set= kwargs.pop('municipality_set', None)
        _union_set = kwargs.pop('union_set', None)
        _wordNo_set = kwargs.pop('wordNo_set', None)
        _village_set = kwargs.pop('village_set', None)
        _mahalla_set = kwargs.pop('mahalla_set', None)
        _block_set = kwargs.pop('block_set', None)
        _holdingNo_set = kwargs.pop('holdingNo_set', None)
        _house_set = kwargs.pop('house_set', None)
        super(PersonForm, self).__init__(*args, **kwargs) 
        self.fields['continent'].widget = ListTextWidget(data_list=_continent_set,name='continent_set')
        self.fields['country'].widget = ListTextWidget(data_list=_country_set,name='country_set')
        self.fields['state'].widget = ListTextWidget(data_list=_state_set,name='state_set')
        self.fields['division'].widget = ListTextWidget(data_list=_division_set,name='division_set')
        self.fields['district'].widget = ListTextWidget(data_list=_district_set,name='district_set')
        self.fields['city'].widget = ListTextWidget(data_list=_city_set,name='city_set')
        self.fields['road_or_streetNo'].widget = ListTextWidget(data_list=_roadOrStreetNo_set,name='roadOrStreetNo_set')
        self.fields['policestation'].widget = ListTextWidget(data_list=_policeStation_set,name='policeStation_set')
        self.fields['postoffice'].widget = ListTextWidget(data_list=_postOffice_set,name='postOffice_set')
        self.fields['zipcode'].widget = ListTextWidget(data_list=_zipCode_set,name='zipCode_set')
        self.fields['upozila_thana'].widget = ListTextWidget(data_list=_thanaUpozila_set,name='thanaUpozila_set')
        self.fields['municipality'].widget = ListTextWidget(data_list=_municipality_set,name='municipality_set')
        self.fields['union'].widget = ListTextWidget(data_list=_union_set,name='union_set')
        self.fields['word_no'].widget = ListTextWidget(data_list=_wordNo_set,name='wordNo_set')
        self.fields['village'].widget = ListTextWidget(data_list=_village_set,name='village_set')
        self.fields['mahalla'].widget = ListTextWidget(data_list=_mahalla_set,name='mahalla_set')
        self.fields['block'].widget = ListTextWidget(data_list=_block_set,name='block_set')
        self.fields['holdingNo'].widget = ListTextWidget(data_list=_holdingNo_set,name='holdingNo_set')
        self.fields['house'].widget = ListTextWidget(data_list=_house_set,name='house_set')
    
  


 