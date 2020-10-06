from django.contrib import messages
from django.shortcuts import render, redirect

from covidtrace.decorator import unauthenticated_user, allowed_users

from .models import *
from.forms import BarangayForm, CitymunForm,EstablishmentForm, VisitorForm, Sys_userForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib import messages

from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def home (request):

    return render(request, 'covidtrace/index.html')

@login_required(login_url='login')
def citymunicipality(request):

    form = CitymunForm()

    context = {"form": form}

    if request.method == "POST":
        form = CitymunForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

        else:
            print("error")


    return render(request, 'covidtrace/citymunicipality.html', context)

@login_required(login_url='login')
def listingbarangay(request):

    barangays = Barangay.objects.all()
    return render(request, 'covidtrace/listingbarangay.html', {"barangays" : barangays})

@login_required(login_url='login')
def listingcitymun(request):

    citymun = Citymun.objects.all()
    return render(request, 'covidtrace/listingcitymun.html', {"citymun" : citymun})

@login_required(login_url= 'login')
def barangay(request):

    form = BarangayForm()

    context = {"form": form}

    if request.method == "POST":
        form = BarangayForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')
            return redirect('/')

        else:
            print("error")


    return render(request, 'covidtrace/barangay.html', context)

@login_required(login_url='login')
def update_Barangay(request, pk):

    barangay = Barangay.objects.get(id = pk)
    form = BarangayForm(instance= barangay)

    if request.method == "POST":
        form = BarangayForm(request.POST, instance= barangay)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')
            return redirect('/')

    context = {'form': form}
    return render(request, 'covidtrace/barangay.html', context)

@login_required(login_url='login')
def delete_Barangay (request, pk):

    barangay = Barangay.objects.get(id = pk)

    if request.method == "POST":
        barangay.delete()
        return redirect('/barangay_listing')

    context = {'item': barangay}
    return render(request, 'covidtrace/delete.html', context)

@login_required(login_url='login')
def update_Citymun(request, pk):

    citymun = Citymun.objects.get(id = pk)
    form = CitymunForm(instance= citymun)

    if request.method == "POST":
        form = CitymunForm(request.POST, instance= citymun)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')
            return redirect('/')

    context = {'form': form}
    return render(request, 'covidtrace/citymunicipality.html', context)

@login_required(login_url='login')
def delete_Citymun (request, pk):

    citymun = Citymun.objects.get(id = pk)

    if request.method == "POST":
        citymun.delete()
        return redirect('/citymun_listing')

    context = {'item': citymun}
    return render(request, 'covidtrace/deletecitymun.html', context)

@unauthenticated_user
def registerUser(request):
    form = UserCreationForm()
    context = {'form': form}

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, 'Account ' + username +' was created')

            if request.method == "POST":
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('/')

                else:
                    return redirect('/login')

            return redirect('/login')



        else:
            return redirect('/')


    return render(request, 'covidtrace/register.html', context)

@unauthenticated_user
def loginuser(request):

    context = {}

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'username or password is incorrect')


    return render(request, 'covidtrace/login.html', context)

@login_required(login_url='login')
def logoutuser(request):
    logout(request)
    return redirect('login')

@login_required
def map(request):
    import folium

    from django.views.decorators.clickjacking import xframe_options_exempt
    barangay = Barangay.objects.all()

    mapa = folium.Map(location=[10.2926, 123.0247], zoom_start=7)

    for barangay in barangay:

        popup = barangay.bname
        latitude = barangay.latitude
        longitude = barangay.longitude
        #
        # folium.Marker([latitude, longitude], popup=popup, tooltip='Click for more info').add_to(mapa)


    cities = Citymun.objects.all()

    for city in cities:

        popup = city.cmdesc
        latitude = city.latitude
        longitude = city.longitude

        folium.Marker(location=[latitude, longitude], popup=popup, color = '#428bca').add_to(mapa)


    mapa.save('covidtrace/templates/covidtrace/map.html')

    context = {'map': mapa}

    return render(request, 'covidtrace/maplayout.html', context)

def mapy(request):

    return render(request, 'covidtrace/map.html')

def create_establishment(request):

    form = EstablishmentForm

    context = {"form": form}

    if request.method == "POST":
        form = EstablishmentForm(request.POST)

        # form.

        if form.is_valid():
            form.save()
            return redirect('/')

        else:
            print(form.errors)


    return render(request, 'covidtrace/establishment.html', context)

def create_visitor(request):

    form = VisitorForm()

    context = {"form": form}

    if request.method == "POST":
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

        else:
            print("error")


    return render(request, 'covidtrace/visitor.html', context)

def create_system_user(request):

    form = EstablishmentForm

    context = {"form": form}

    if request.method == "POST":
        form = EstablishmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

        else:
            print("error")


    return render(request, 'covidtrace/create_user.html', context)