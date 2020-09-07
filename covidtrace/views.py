from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from.forms import BarangayForm, CitymunForm


def home (request):

    return render(request, 'covidtrace/index.html')


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


def listingbarangay(request):

    barangays = Barangay.objects.all()
    return render(request, 'covidtrace/listingbarangay.html', {"barangays" : barangays})


def listingcitymun(request):

    citymun = Citymun.objects.all()
    return render(request, 'covidtrace/listingcitymun.html', {"citymun" : citymun})


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


def delete_Barangay (request, pk):

    barangay = Barangay.objects.get(id = pk)

    if request.method == "POST":
        barangay.delete()
        return redirect('/barangay_listing')

    context = {'item': barangay}
    return render(request, 'covidtrace/delete.html', context)