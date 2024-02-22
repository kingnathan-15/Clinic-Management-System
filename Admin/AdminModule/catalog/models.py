from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
import datetime

class Patient(models.Model):
    #user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
class Physician(models.Model):
    #user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    staff_id = models.IntegerField(unique=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    time_available = []

    start_hour = 7
    end_hour = 21  # 9 pm in 24-hour format

    for hour in range(start_hour, end_hour):
        for minute in range(0, 60, 15):
            start_time = f"{hour:02d}:{minute:02d}"
            end_time = f"{hour:02d}:{(minute + 15) % 60:02d}"
            time_range = f"{start_time}-{end_time}"
            time_available.append((time_range, start_time))

    appointment_date = models.DateField(null=True, blank=True)
    appointment_time = models.TimeField(
        choices=time_available,
        blank=True,
        default="7:00",
        help_text="Choose time interval")
    patient_attending = models.ForeignKey(Patient, on_delete=models.SET_NULL,
                                          null=True, blank=True)
    attending_physician = models.ForeignKey(Physician, on_delete=models.SET_NULL,
                                          null=True, blank=True)
    Apps_stat = (
        ('u', 'Unconfirmed'),
        ('c', 'Confirmed'),
        ('r', 'Cancelled'),
        ('a', 'Attended'),
    )
    status = models.CharField(
        max_length=1,
        choices=Apps_stat,
        blank=True,
        default='u',
        help_text='Whether the appointment has been confirmed or not'
    )

    def __str__(self):
        return self.dt

class PharmacyInventory(models.Model):
    name = models.CharField(max_length = 50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    amount_available = models.IntegerField(default=0)
    image = models.ImageField(upload_to='uploads/product/', blank=True)

    def __str__(self):
        return self.name

class Prescription(models.Model):
    patient_name = models.ForeignKey(User, on_delete=models.SET_NULL,
                                          null=True, blank=True)
    medicine = models.ForeignKey("PharmacyInventory", on_delete=models.SET_NULL, null=True)
    total_amount=models.IntegerField(default=0)
    #total_price = total_amount*medicine.objects.filter(medicine__price="John")
    stat =(
        ('p', 'Pending'),
        ('f', 'Fulfilled'),
    )

    status = models.CharField(
        max_length=1,
        choices=stat,
        blank=True,
        default='p',
    )


