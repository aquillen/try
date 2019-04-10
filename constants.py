# Needed constants

Semi_major_Pan = 133584.0E3 #in m from km
G = 6.67408E−11 #units m^2 kg-1 s-2  # gravitational constant
#angular rotation rate of Pan in orbit, this gives our Coriolis force, mean motion
n_Pan = np.sqrt(G*Saturn_mass/Semi_major_Pan**3)
R_polar_Pan =20.8e3  # polar radius of Pan in m


