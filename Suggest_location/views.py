from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import PersonForm
from .models import District, Country, Continent

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
        
            # redirect to a new URL:
            # return HttpResponseRedirect('/thanks/')
            

            return HttpResponse("Success!")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PersonForm(district_set = District.objects.all().order_by("name"),country_set = Country.objects.all().order_by("name"),continent_set = Continent.objects.all().order_by("name"))


    return render(request, 'index.html', context={'form': form})




# from django.core.mail import send_mail

# if form.is_valid():
#     subject = form.cleaned_data['subject']
#     message = form.cleaned_data['message']
#     sender = form.cleaned_data['sender']
#     cc_myself = form.cleaned_data['cc_myself']

#     recipients = ['info@example.com']
#     if cc_myself:
#         recipients.append(sender)

#     send_mail(subject, message, sender, recipients)
#     return HttpResponseRedirect('/thanks/')

