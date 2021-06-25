from django.db import models

class Continent(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    topLevelDomain = models.CharField(max_length=250, blank=True, null=True)
    alpha2Code = models.CharField(max_length=250, blank=True, null=True)
    alpha3Code = models.CharField(max_length=250, blank=True, null=True)
    callingCodes = models.CharField(max_length=250, blank=True, null=True)
    capital = models.CharField(max_length=250, blank=True, null=True)
    region = models.CharField(max_length=250, blank=True, null=True)
    subregion = models.CharField(max_length=250, blank=True, null=True)
    latlng = models.CharField(max_length=250, blank=True, null=True)
    demonym = models.CharField(max_length=250, blank=True, null=True)
    area = models.CharField(max_length=250, blank=True, null=True)
    timezones = models.CharField(max_length=250, blank=True, null=True)
    currencies = models.TextField(blank=True, null=True)
    languages = models.TextField(blank=True, null=True)
    flag = models.CharField(max_length=250, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    currencies_code = models.CharField(max_length=250, blank=True, null=True)
    currencies_name = models.CharField(max_length=250, blank=True, null=True)
    currencies_symbol = models.CharField(max_length=250, blank=True, null=True)

    continent = models.ForeignKey(Continent, blank=True, null=True, on_delete=models.CASCADE, related_name='country_continentList')

    def __str__(self):
        return self.name


        
class State(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    country= models.ForeignKey(Country, blank=True, null=True, related_name='state_countryList', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Division(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    state= models.ForeignKey(State, blank=True, null=True, related_name='division_stateList', on_delete=models.CASCADE)
    country= models.ForeignKey(Country, blank=True, null=True, related_name='division_countryList', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    division= models.ForeignKey(Division, blank=True, null=True, related_name='district_divisionList', on_delete=models.CASCADE)
    country= models.ForeignKey(Country, blank=True, null=True, related_name='district_countryList', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    district= models.ForeignKey(District, blank=True, null=True, related_name='city_districtList', on_delete=models.CASCADE)
    state= models.ForeignKey(State, blank=True, null=True, related_name='city_stateList', on_delete=models.CASCADE)
    country= models.ForeignKey(Country, blank=True, null=True, related_name='city_countryList', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Road_or_Street_No(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    district= models.ForeignKey(District, blank=True, null=True, related_name='roadno_districtList', on_delete=models.CASCADE)
    city= models.ForeignKey(City, blank=True, null=True, related_name='roadno_cityList', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class PoliceStation(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    district= models.ForeignKey(District, blank=True, null=True, related_name='policeStation_districtList', on_delete=models.CASCADE)
    city= models.ForeignKey(City, blank=True, null=True, related_name='policeStation_cityList', on_delete=models.CASCADE)
    def __str__(self):
        return self.name



class PostOffice(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    district= models.ForeignKey(District, blank=True, null=True, related_name='postoffice_districtList', on_delete=models.CASCADE)
    city= models.ForeignKey(City, blank=True, null=True, related_name='postoffice_cityList', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class PostCode_or_ZipCode(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    district= models.ForeignKey(District, blank=True, null=True, related_name='zipcode_districtList', on_delete=models.CASCADE)
    city= models.ForeignKey(City, blank=True, null=True, related_name='zipcode_cityList', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class ThanaUpozila(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    district= models.ForeignKey(District, blank=True, null=True, related_name='thana_districtList', on_delete=models.CASCADE)
    city= models.ForeignKey(City, blank=True, null=True, related_name='thana_cityList', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Municipality(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    thana = models.ForeignKey(ThanaUpozila, blank=True, null=True, related_name='municipality_ThanaList', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Union(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    thana = models.ForeignKey(ThanaUpozila, blank=True, null=True, related_name='union_ThanaList', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class WordNo(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    thana = models.ForeignKey(ThanaUpozila, blank=True, null=True, related_name='wordno_ThanaList', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Village(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    union = models.ForeignKey(Union, blank=True, null=True, related_name='village_unionList', on_delete=models.CASCADE)
    municipality = models.ForeignKey(Municipality, blank=True, null=True, related_name='village_municipalityList', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Mahalla(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    village = models.ForeignKey(Village, blank=True, null=True, related_name='mahalla_villageList', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Block(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    village = models.ForeignKey(Village, blank=True, null=True, related_name='block_villageList', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class HoldingNo(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    village = models.ForeignKey(Village, blank=True, null=True, related_name='holdingNo_villageList', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class House(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    village = models.ForeignKey(Village, blank=True, null=True, related_name='house_villageList', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


