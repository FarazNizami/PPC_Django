from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import BlastPressure,BlastFlow, CppPciWeights, Temperature, Press

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
  
    latest_blast_pressure = BlastPressure.objects.order_by('').first()
    latest_blast_flow = BlastFlow.objects.order_by('').first()
    latest_cpp_pci_weights = CppPciWeights.objects.order_by('').first()
    latest_temperature = Temperature.objects.order_by('').first()
    latest_press = Press.objects.order_by('').first()


  