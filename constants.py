# Needed constants

import numpy as np

mass_Saturn = 5.683E26 # kg
mass_Pan = 4.95E15 # kg
Semi_major_Pan = 133584.0E3 #in m from km
G = 6.67408E-11 #units m^2 kg-1 s-2  # gravitational constant
#angular rotation rate of Pan in orbit, this gives our Coriolis force, mean motion
n_Pan = np.sqrt(G*mass_Saturn/Semi_major_Pan**3)
R_polar_Pan =10.4e3  # polar radius of Pan in m

r_Hill_Pan = Semi_major_Pan*(mass_Pan/(3*mass_Saturn))**(1.0/3.0)  #Hill radius of Pan
