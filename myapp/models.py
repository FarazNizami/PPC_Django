from django.db import models
from django.utils import timezone


class BlastPressure(models.Model):
    cold_blast_pressure = models.FloatField(null=True, blank=True)
    hot_blast_pressure = models.FloatField(null=True, blank=True)
    cold_blast_flow = models.FloatField(null=True, blank=True)
    hot_blast_flow = models.FloatField(null=True, blank=True)
    hot_blast_temperature = models.FloatField(null=True, blank=True)
    raft = models.FloatField(null=True, blank=True)
    new_calc = models.FloatField(null=True, blank=True)
    top_pressure = models.FloatField(null=True, blank=True)
    d_pressure_burden = models.FloatField(null=True, blank=True)
    discharge_level = models.FloatField(null=True, blank=True)
    current_burden_level = models.FloatField(null=True, blank=True)
    moisture_in_hot_blast = models.FloatField(null=True, blank=True)
    coal_injection_rate = models.FloatField(null=True, blank=True)
    coal_injection_rate_ton = models.FloatField(null=True, blank=True)
    sp = models.FloatField(null=True, blank=True)
    oxygen_injection = models.FloatField(null=True, blank=True)
    top_dp = models.FloatField(null=True, blank=True)
    mid_dp = models.FloatField(null=True, blank=True)
    bottom_dp = models.FloatField(null=True, blank=True)
    bottom_k = models.FloatField(null=True, blank=True)
    mid_k = models.FloatField(null=True, blank=True)
    permeability_k_sum = models.FloatField(null=True, blank=True)
    charge_shift_a = models.IntegerField(null=True, blank=True)
    charge_shift_b = models.IntegerField(null=True, blank=True)
    charge_shift_c = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)


   #  Blast Flow Model
class BlastFlow(models.Model):
    hot_metal_temp_th1 = models.FloatField(null=True, blank=True)
    hot_metal_temp_th2 = models.FloatField(null=True, blank=True)
    hot_metal_temp_th3 = models.FloatField(null=True, blank=True)
    hot_metal_temp_th4 = models.FloatField(null=True, blank=True)

    uptake_temp_a = models.FloatField(null=True, blank=True)
    uptake_temp_b = models.FloatField(null=True, blank=True)
    uptake_temp_c = models.FloatField(null=True, blank=True)
    uptake_temp_d = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
   #  Temperature Model
class Temperature(models.Model):
    tuyere_cooling_total_flow = models.FloatField(null=True, blank=True)
    tuyere_cooling_pressure_1 = models.FloatField(null=True, blank=True)
    tuyere_cooling_pressure_2 = models.FloatField(null=True, blank=True)
    tuyere_cooling_tank_level = models.FloatField(null=True, blank=True)

    stack_cooling_total_flow = models.FloatField(null=True, blank=True)
    stack_cooling_pressure = models.FloatField(null=True, blank=True)
    stack_cooling_tank_level = models.FloatField(null=True, blank=True)

    hearth_bottom_total_flow = models.FloatField(null=True, blank=True)
    hearth_bottom_pressure = models.FloatField(null=True, blank=True)
    hearth_bottom_tank_level = models.FloatField(null=True, blank=True)

    secondary_cooling_total_flow = models.FloatField(null=True, blank=True)
    secondary_cooling_pressure = models.FloatField(null=True, blank=True)
    secondary_cooling_tank_level = models.FloatField(null=True, blank=True)

    blt_cooling_flow_total_flow = models.FloatField(null=True, blank=True)
    blt_cooling_tank_level = models.FloatField(null=True, blank=True)

    heat_load_total_flow = models.FloatField(null=True, blank=True)
    heat_load_pressure = models.FloatField(null=True, blank=True)
    heat_load_tank_level = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
   #  CPP/PCI Weights Model
class CppPciWeights(models.Model):
    feed_tank_1 = models.FloatField(null=True, blank=True)
    pci_n2_supply_pr = models.FloatField(null=True, blank=True)
    feed_tank_2 = models.FloatField(null=True, blank=True)
    inst_supply_pr = models.FloatField(null=True, blank=True)
    feed_tank_3  = models.FloatField(null=True, blank=True)
    lances_on_coal = models.IntegerField(null=True, blank=True)
    fcs_weight = models.FloatField(null=True, blank=True)
    hmt_production = models.FloatField(null=True, blank=True)
    rcs_1_weight = models.FloatField(null=True, blank=True)
    rcs_2_weight = models.FloatField(null=True, blank=True)
    low_pressure_n2 = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

     #  PRESS Model
class Press(models.Model):
    ff_spray_press = models.FloatField(null=True, blank=True)
    ff_hyd_press = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

  
