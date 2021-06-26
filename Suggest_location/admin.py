from django.contrib import admin

# Register your models here.
from  .models import Person, Continent, Country, State, Division, District, City, Road_or_Street_No, PoliceStation, PostOffice,PostCode_or_ZipCode, ThanaUpozila, Municipality, Union, WordNo, Village, Mahalla, Block, HoldingNo, House

# Register your models here.
admin.site.register([Person, Continent, Country, State, Division, District, City, Road_or_Street_No, PoliceStation, PostOffice,PostCode_or_ZipCode, ThanaUpozila, Municipality, Union, WordNo, Village, Mahalla, Block, HoldingNo, House
])