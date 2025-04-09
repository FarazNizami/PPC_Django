from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from .models import BlastPressure, BlastFlow, CppPciWeights, Temperature, Press

def home(request):
    return render(request, 'layout/base.html')

# Render the Blast Furnace Monitoring Page
def blastfurnace(request):
    # Fetch the latest data for rendering
    latest_blast_pressure = BlastPressure.objects.order_by('-id').first()
    latest_blast_flow = BlastFlow.objects.order_by('-id').first()
    latest_cpp_pci_weights = CppPciWeights.objects.order_by('-id').first()
    latest_temperature = Temperature.objects.order_by('-id').first()
    latest_press = Press.objects.order_by('-id').first()

    return render(request, 'pages/blast_furnace.html',
     {
        'latest_blast_pressure': latest_blast_pressure,
        'latest_blast_flow': latest_blast_flow,
        'latest_cpp_pci_weights': latest_cpp_pci_weights,
        'latest_temperature': latest_temperature,
        'latest_press' : latest_press,
    })

def get_latest_data(request):
    latest_blast_pressure = BlastPressure.objects.order_by('-id').first()
    latest_blast_flow = BlastFlow.objects.order_by('-id').first()
    latest_cpp_pci_weights = CppPciWeights.objects.order_by('-id').first()
    latest_temperature = Temperature.objects.order_by('-id').first()
    latest_press = Press.objects.order_by('-id').first()
    return JsonResponse({
        'latest_blast_pressure': latest_blast_pressure,
        'latest_blast_flow': latest_blast_flow,
        'latest_cpp_pci_weights': latest_cpp_pci_weights,
        'latest_temperature': latest_temperature,
        'latest_press' : latest_press,
    })

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login')
            return render(request, 'pages/login.html')
    else:
        return render(request, 'pages/login.html')