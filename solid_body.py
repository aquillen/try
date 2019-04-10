import numpy as np
#import particle 

class stuck_particle():
  #constructor
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
    
  #part_list is a list of particle objects
  #axis: 0=x, 1=y, 2=z
  def rotate(part_list, axis, angle):
      rotated_list = part_list
      
      #rotating about x
      def x():
          return
      
      #rotating about y
      def y():
          return
      
      #rotating about z
      def z():
          return
      
      #switch statement to determine which function to call depending on axis
      switcher = {
              0: x,
              1: y,
              2: z
        }
      
      def num_to_func(axis):
          func = switcher.get(axis, "DEFAULT")
          return func()
   
    
  
  def recenter():
      
      return

