from django.contrib import admin
from .models import BlastPressure, BlastFlow, Temperature, CppPciWeights, Press

admin.site.register(BlastPressure)
admin.site.register(BlastFlow)
admin.site.register(Temperature)
admin.site.register(CppPciWeights)
admin.site.register(Press)
