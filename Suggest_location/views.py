from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import PersonForm
from .models import Person, Continent, Country, State, Division, District, City, Road_or_Street_No, PoliceStation, PostOffice,PostCode_or_ZipCode, ThanaUpozila, Municipality, Union, WordNo, Village, Mahalla, Block, HoldingNo, House


# Create your views here.
def IndexView(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            continent = form.cleaned_data['continent']
            country = form.cleaned_data['country']
            district = form.cleaned_data['district']
            print("Name:", name,"Phone:",phone,"email:", email,"continent:",continent,"country:", country,"district:",district )
        
            # redirect to a new URL:
            # return HttpResponseRedirect('/thanks/')
            

            return HttpResponse("Success!")

    # if a GET (or any other method) we'll create a blank form
    else:
        

        form = PersonForm(
            continent_set = Continent.objects.all().order_by("name"),
            country_set = Country.objects.all().order_by("name"), 
            state_set = State.objects.all().order_by("name"),
            division_set = Division.objects.all().order_by("name"),
            district_set = District.objects.all().order_by("name"),
            city_set = City.objects.all().order_by("name"),
            roadOrStreetNo_set = Road_or_Street_No.objects.all().order_by("name"),
            policeStation_set = PoliceStation.objects.all().order_by("name"),
            postOffice_set = PostOffice.objects.all().order_by("name"),
            zipCode_set = PostCode_or_ZipCode.objects.all().order_by("name"),
            thanaUpozila_set = ThanaUpozila.objects.all().order_by("name"),
            municipality_set = Municipality.objects.all().order_by("name"),
            union_set = Union.objects.all().order_by("name"),
            wordNo_set = WordNo.objects.all().order_by("name"),
            village_set = Village.objects.all().order_by("name"),
            mahalla_set = Mahalla.objects.all().order_by("name"),
            block_set = Block.objects.all().order_by("name"),
            holdingNo_set = HoldingNo.objects.all().order_by("name"),
            house_set = House.objects.all().order_by("name"),)

    return render(request, 'index.html', context={'form': form})



