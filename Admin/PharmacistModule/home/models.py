from django.db import models
import datetime

# Create your models here.

class Prescription(models.Model):
    patient_name = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    dosage = models.CharField(max_length = 10)
    image = models.ImageField(upload_to='uploads/product/', blank=True)


