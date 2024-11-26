from django.shortcuts import render, redirect
from .models import Patient


def list_patients(request):
    patients = Patient.objects.all()  
    return render(request, 'patients/list_patients.html', {'patients': patients})

# Função para criar um novo paciente
def create_patient(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        cpf = request.POST.get('cpf')
        phone = request.POST.get('phone')
        Patient.objects.create(name=name, age=age, cpf=cpf, phone=phone)
        return redirect('list_patients')  
    return render(request, 'patients/create_patient.html')  
