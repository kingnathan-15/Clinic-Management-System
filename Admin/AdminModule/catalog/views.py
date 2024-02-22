from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# tseest
# Create your views here.
from .models import *
from .forms import *
from .decorators import unauthenticated_user, allowed_users, admin_only


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='Pharmacists')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)

            return redirect('log-in')

    context = {'form': form}
    return render(request, 'registration/signup.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'registration/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('log-in')


@login_required(login_url='log-in')
@admin_only
def index(request):

    num_appointments = Appointment.objects.count()

    context = {
        'num_appointments': num_appointments
    }

    return render(request, 'index.html', context=context)

@login_required(login_url='log-in')
@allowed_users(allowed_roles=['Physicians'])
def physicianPage(request):
    context = {}
    return render(request, 'physician/physician.html', context)

@login_required(login_url='log-in')
@allowed_users(allowed_roles=['Patients'])
def patientPage(request):
    #appointments = request.user.patient.appointment_set.all()
    #prescriptions = request.user.patient.prescription_set.all()
    context = {}
    return render(request, 'patients/patient.html', context)

@login_required(login_url='log-in')
@allowed_users(allowed_roles=['Pharmacists'])
def pharmacistPage(request):
    inventory = PharmacyInventory.objects.all()
    context = {'inventory': inventory}
    return render(request, 'pharmacist/pharmacist.html', context)


def createAppointment(request):

    form = AppointmentForm()
    if request.method == "POST":
        print('Printing POST:', request.POST)

    context = {'form': form}
    return render(request, 'patients/appointment_form.html', context)

def createPrescription(request):
    form = PrescriptionForm()
    if request.method == "POST":
        form=PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'physician/prescription_form.html', context)

def createInventory(request):
    form = InventoryForm()
    if request.method == "POST":
        print('Printing POST:', request.POST)

    context = {'form': form}
    return render(request, 'pharmacist/inventory.html', context)


def updateAppointment(request):

    return render(request)
def updatePrescription(request, pk):
    order = Prescription.objects.get(id=pk)
    form = PrescriptionForm(instance=Prescription)

    if request.method == 'POST':
        form = PrescriptionForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'pharmacist/pharmacist.html', context)
def updateInventory(request, pk):
    order = Prescription.objects.get(id=pk)
    form = PrescriptionForm(instance=Prescription)

    if request.method == 'POST':
        form = PrescriptionForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'pharmacist/inventory2.html', context)

def deleteAppointment(request):
    return render(request)
def deletePrescription(request):
    return render(request)
def deleteInventory(request):
    return render(request)