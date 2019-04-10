import numpy as np
import particle 

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
          for i in range(0,len(part_list)):
              #getting attributes from object
              x0 = getattr(part_list[i], 'x')
              y0 = getattr(part_list[i], 'y')
              z0 = getattr(part_list[i], 'z')
              
              #rotation
              y1 = y0*np.cos(angle)-z0*np.sin(angle)
              z1 = y0*np.sin(angle)+z0*np.cos(angle)
              x1 = x0
              
              #setting particle attributes to rotated values
              setattr(part_list[i], 'x', x1)
              setattr(part_list[i], 'y', y1)
              setattr(part_list[i], 'y', z1)
              
          return #not sure what to return since this would be a destructive void method
      
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
      
      #inner function to convert axis num to function
      def num_to_func(axis):
          func = switcher.get(axis, "DEFAULT")
          return func()
      
      rotated_list = num_to_func(axis)
      return rotated_list
  
  def recenter():
      
      return

