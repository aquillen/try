import numpy as np
import particle
import constants

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
  
  # add a new particle to the list of stuck particles
  def add_particle(self,mass,radius,x,y,z):
    self.N+=1
    s_particle = stuck_particle(mass,radius,x,y,z)
    self.stuck_particles =np.append(self.stuck_particles,s_particle)
  
  #axis: 0=x, 1=y, 2=z
  def rotate(self,axis, angle):  # no need to pass particle list as this is defined within solid_body class
      rotated_list = part_list
      
      #rotating about x
      def x():
          for i in range(0,len(self.stuck_particles)):
              #getting attributes from object
              x0 = getattr(self.stuck_particles[i], 'x')
              y0 = getattr(self.stuck_particles[i], 'y')
              z0 = getattr(self.stuck_particles[i], 'z')
              
              #rotation
              y1 = y0*np.cos(angle)-z0*np.sin(angle)
              z1 = y0*np.sin(angle)+z0*np.cos(angle)
              x1 = x0
              
              #setting particle attributes to rotated values
              setattr(self.stuck_particles[i], 'x', x1)
              setattr(self.stuck_particles[i], 'y', y1)
              setattr(self.stuck_particles[i], 'y', z1)
              
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
      
      # compute center of mass and subtract it from all particle positions
      def recenter(self):
          sumx = 0
          sumy = 0
          sumz = 0
          msum = 0
          n = len(self.stuck_particles)
          for i in range(0,n):  # sums are used to compute expection of x,y,z
              sumx += self.stuck_particles[i].x * self.stuck_particles[i].m
              sumy += self.stuck_particles[i].y * self.stuck_particles[i].m
              sumz += self.stuck_particles[i].z * self.stuck_particles[i].m
              msum += self.stuck_particles[i].m
    
          #compute center of mass
          meanx = sumx/msum
          meany = sumy/msum
          meanz = sumz/msum
          # subtract center of mass from all particle positions
          for i in range(0,n):
              self.stuck_particles[i].x -= meanx
              self.stuck_particles[i].y -= meany
              self.stuck_particles[i].z -= meanz
      

#rotated_list = num_to_func(axis)
#return rotated_list
