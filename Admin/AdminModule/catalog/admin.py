from django.contrib import admin
from .models import *

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appointment_date', 'appointment_time', 'patient_attending', 'status', 'attending_physician')
    fields = ['patient_attending','attending_physician','status', ('appointment_date', 'appointment_time')]

admin.site.register(Prescription)
admin.site.register(PharmacyInventory)
admin.site.register(Patient)
admin.site.register(Physician)