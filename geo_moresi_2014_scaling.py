#!/usr/bin/env python
# coding: utf-8

# **Scaling**

# In[1]:


import UWGeodynamics as GEO

from UWGeodynamics.scaling import units as u
from UWGeodynamics.scaling import dimensionalise, non_dimensionalise
from UWGeodynamics.scaling import non_dimensionalise as nd


# In[3]:


GEO.__file__


# In[4]:


import geo_model_properties as modprop
import geo_material_properties as matprop


# In[5]:


dRho =   80. * u.kilogram / u.meter**3 # matprop.ref_density
g    =   10. * u.meter / u.second**2   # modprop.gravity
H    = 1000. * u.kilometer #  modprop.boxHeight

# lithostatic pressure for mass-time-length
ref_stress = dRho * g * H
# viscosity of upper mante for mass-time-length
ref_viscosity = 1e20 * u.pascal * u.seconds


# In[6]:


ref_time        = ref_viscosity/ref_stress
ref_length      = H
ref_mass        = (ref_viscosity*ref_length*ref_time).to_base_units()
ref_temperature = modprop.Tint - modprop.Tsurf


# In[7]:


KL = ref_length       
KM = ref_mass         
Kt = ref_time
KT = ref_temperature

scaling_coefficients = GEO.scaling.get_coefficients()
# scaling_coefficients = uw.scaling.get_coefficients()

scaling_coefficients["[length]"] = KL.to_base_units()
scaling_coefficients["[time]"]   = Kt.to_base_units()
scaling_coefficients["[mass]"]   = KM.to_base_units()
scaling_coefficients["[temperature]"]   = KT.to_base_units()


# In[8]:


scaling_coefficients


# In[ ]:




