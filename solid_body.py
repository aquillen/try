import numpy as np

class stuck_particle():
  constructor
  def __init__(self,mass,radius,x,y,z):
    self.x = x
    self.y = y
    self.z = z
    self.mass = mass
    self.radius = radius

class solid_body():
  #constructor, construct with a single central stuck particle
  def __init__(self,mass,radius):
    self.N=1  # how many particles in the solid body
    self.stuck_particles = []
    first_particle = stuck_particle(mass,radius,0,0,0)
    self.stuck_particles = np.append(self.stuck_particles,first_particle)
    
  
  
  

