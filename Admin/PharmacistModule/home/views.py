from django.shortcuts import render, redirect
from .models import Prescription
from django.contrib import messages
# Create your views here.

def home(request):
    prescriptions = Prescription.objects.all()
    return render(request,'home.html', {'prescriptions':prescriptions})


    pre = pre(request)
    if request.POST.get('action') == 'post':
        # get stuff
        Prescription_id = request.POST.get('Prescription_id')

        # delete funtion
        pre.delete(Prescription=Prescription_id)

        response = JsonResponse({'Prescription': Prescription_id})
        messages.success(request, ("Item deleted from pre"))
        return response