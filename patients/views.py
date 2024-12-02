from django.shortcuts import render, redirect
from .models import Patient, Doctor

def home(request):
    return render(request, 'tempaltes/patients/home.html')



def list_patients(request):
    patients = Patient.objects.all()  
    return render(request, 'patients/list_patients.html', {'patients': patients})


def create_patient(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        cpf = request.POST.get('cpf')
        phone = request.POST.get('phone')
        Patient.objects.create(name=name, age=age, cpf=cpf, phone=phone)
        return redirect('list_patients')  
    return render(request, 'patients/create_patient.html')  



def list_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'patients/list_doctors.html', {'doctors': doctors})