from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class AppointmentForm(ModelForm):
	class Meta:
		model = Appointment
		fields = '__all__'

class PrescriptionForm(ModelForm):
	class Meta:
		model = Prescription
		fields = '__all__'

class InventoryForm(ModelForm):
	class Meta:
		model = PharmacyInventory
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']