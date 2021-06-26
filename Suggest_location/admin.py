from django.contrib import admin

# Register your models here.
from  .models import Person, Continent, Country,  District

# Register your models here.
admin.site.register([Person, Continent, Country, District])