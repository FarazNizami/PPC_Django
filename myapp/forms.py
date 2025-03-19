from django import forms
from .models import BlastPressure ,BlastFlow ,Temperature ,CppPciWeights, Press

class BlastPressureForm(forms.ModelForm):
    class Meta:
        model = BlastPressure
        fields = '__all__'  # Use all fields from the model

class BlastFlowForm(forms.ModelForm):
    class Meta:
        model = BlastFlow
        fields = '__all__'  # Use all fields from the model

class TemperatureForm(forms.ModelForm):
    class Meta:
        model = Temperature
        fields = '__all__'  # Use all fields from the model

class CppPciWeightsForm(forms.ModelForm):
    class Meta:
        model = CppPciWeights
        fields = '__all__'  # Use all fields from the model

class PressForm(forms.ModelForm):
    class Meta:
        model = Press
        fields = '__all__'  # Use all fields from the model
