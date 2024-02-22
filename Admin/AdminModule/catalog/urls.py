from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="log-in"),
    path('logout/', views.logoutUser, name="log-out"),
    path('patient/', views.patientPage, name="patient-page"),
    path('pharmacist/', views.pharmacistPage, name="pharmacist-page"),
    path('physician/', views.physicianPage, name="physician-page"),

    path('create_appointment/', views.createAppointment, name="create_Appointments"),
    path('create_prescription/', views.createPrescription, name="create_Prescription"),
    path('create_inventory/', views.createInventory, name="create_Inventory"),
    path('update_appointment/<str:pk>/', views.updateAppointment, name="update_Appointments"),
    path('update_prescription/<str:pk>/', views.updatePrescription, name="update_Prescription"),
    path('update_inventory/<str:pk>/', views.updateInventory, name="update_Inventory"),
    path('delete_appointment/', views.deleteAppointment, name="delete_Appointments"),
    path('delete_prescription/', views.deletePrescription, name="delete_Prescription"),
    path('delete_inventory/', views.deleteInventory, name="delete_Inventory"),

    path('', views.index, name="index"),
]