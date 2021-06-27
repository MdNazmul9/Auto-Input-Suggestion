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
            state = form.cleaned_data['state']
            division = form.cleaned_data['division']
            district = form.cleaned_data['district']
            city = form.cleaned_data['city']
            road_or_streetNo =form.cleaned_data['road_or_streetNo']
            policestation =form.cleaned_data['policestation']
            postoffice =form.cleaned_data['postoffice']
            zipcode =form.cleaned_data['zipcode']
            upozila_thana =form.cleaned_data['upozila_thana']
            municipality =form.cleaned_data['municipality']
            union =form.cleaned_data['union']
            word_no =form.cleaned_data['word_no']
            village =form.cleaned_data['village']
            mahalla =form.cleaned_data['mahalla']
            block =form.cleaned_data['block']
            holdingNo =form.cleaned_data['holdingNo']
            house =form.cleaned_data['house']

            person = Person(
                name = name,
                phone = phone,
                email = email,
                continent = continent,
                country = country,
                state = state,
                division = division,
                district = district,
                city = city,
                road_or_streetNo = road_or_streetNo,
                policestation = policestation,
                postoffice = postoffice,
                zipcode = zipcode,
                upozila_thana =upozila_thana,
                municipality =municipality,
                union = union,
                word_no = word_no,
                village = village,
                mahalla = mahalla,
                block =block,
                holdingNo =holdingNo,
                house =house,
            )
            person.save()

            # person.name = form.cleaned_data['name']
            # person.phone = form.cleaned_data['phone']
            # person.email = form.cleaned_data['email']
            # person.continent = form.cleaned_data['continent']
            # person.country = form.cleaned_data['country']
            # person.state = form.cleaned_data['state']
            # person.division = form.cleaned_data['division']
            # person.district = form.cleaned_data['district']
            # person.city = form.cleaned_data['city']
            # person.road_or_streetNo =form.cleaned_data['road_or_streetNo']
            # person.policestation =form.cleaned_data['policestation']
            # person.postoffice =form.cleaned_data['postoffice']
            # person.zipcode =form.cleaned_data['zipcode']
            # person.upozila_thana =form.cleaned_data['upozila_thana']
            # person.municipality =form.cleaned_data['municipality']
            # person.union =form.cleaned_data['union']
            # person.word_no =form.cleaned_data['word_no']
            # person.village =form.cleaned_data['village']
            # person.mahalla =form.cleaned_data['mahalla']
            # person.block =form.cleaned_data['block']
            # person.holdingNo =form.cleaned_data['holdingNo']
            # person.house =form.cleaned_data['house']

            if state!= None:
                if not State.objects.filter(name=state).exists():
                    state_obj = State(name=state)
                    state_obj.save()

            if division!= None:       
                if not Division.objects.filter(name=division).exists():
                    division_obj = City(name=division)
                    division_obj.save()


            if district!= None:
                if not District.objects.filter(name=district).exists():
                    district_obj = District(name=district)
                    district_obj.save()

            if city!= None:       
                if not City.objects.filter(name=city).exists():
                    city_obj = City(name=city)
                    city_obj.save()

            
            if road_or_streetNo != None:       
                if not Road_or_Street_No.objects.filter(name=road_or_streetNo).exists():
                    road_or_streetNo_obj = Road_or_Street_No(name=road_or_streetNo)
                    road_or_streetNo_obj.save()

           
            if policestation != None:       
                if not PoliceStation.objects.filter(name=policestation).exists():
                    policestation_obj = PoliceStation(name=policestation)
                    policestation_obj.save()


            if postoffice != None:       
                if not PostOffice.objects.filter(name=postoffice).exists():
                    postoffice_obj = PostOffice(name=postoffice)
                    postoffice_obj.save()
            
            if zipcode != None:       
                if not PostCode_or_ZipCode.objects.filter(name=zipcode).exists():
                    zipcode_obj = PostCode_or_ZipCode(name=zipcode)
                    zipcode_obj.save()

            if upozila_thana != None:       
                if not ThanaUpozila.objects.filter(name=upozila_thana).exists():
                    upozila_thana_obj = ThanaUpozila(name=upozila_thana)
                    upozila_thana_obj.save()


            if municipality != None:       
                if not Municipality.objects.filter(name=municipality).exists():
                    municipality_obj = Municipality(name=municipality)
                    municipality_obj.save()
            
            if union != None:       
                if not Union.objects.filter(name=road_or_streetNo).exists():
                    union_obj = Union(name=road_or_streetNo)
                    union_obj.save()
            
            if word_no != None:       
                if not WordNo.objects.filter(name=word_no).exists():
                    word_no_obj = WordNo(name=word_no)
                    word_no_obj.save()

            if village != None:       
                if not Village.objects.filter(name=village).exists():
                    village_obj = Village(name=village)
                    village_obj.save()


            if mahalla != None:       
                if not Mahalla.objects.filter(name=mahalla).exists():
                    mahalla_obj = Mahalla(name=mahalla)
                    mahalla_obj.save()

            if block != None:       
                if not Block.objects.filter(name=block).exists():
                    block_obj = Block(name=block)
                    block_obj.save()

            if holdingNo != None:       
                if not HoldingNo.objects.filter(name=holdingNo).exists():
                    holdingNo_obj = HoldingNo(name=holdingNo)
                    holdingNo_obj.save()
            
            if house != None:       
                if not House.objects.filter(name=house).exists():
                    house_obj = House(name=house)
                    house_obj.save()

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



