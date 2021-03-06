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


# I think I need to call this class something other than the file name, otherwise I got an error!
class Psolid_body():
    #constructor, construct with a single central stuck particle
    def __init__(self,mass,radius):
        self.N=1  # how many particles in the solid body
        self.stuck_particles = []
        first_particle = stuck_particle(mass,radius,0,0,0)
        self.stuck_particles = np.append(self.stuck_particles,first_particle)
  
    # add a new particle to the list of stuck particles
    @staticmethod
    def add_particle(self,mass,radius,x,y,z):
        self.N+=1
        s_particle = stuck_particle(mass,radius,x,y,z)
        self.stuck_particles =np.append(self.stuck_particles,s_particle)

    # compute center of mass and subtract it from all particle positions
    @staticmethod
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


    #axis: 0=x, 1=y, 2=z
    @staticmethod
    def rotate(self,axis, angle):  # no need to pass particle list as this is defined within solid_body class
        #rotated_list = part_list
        if(axis == 0):
            Psolid_body.Rx(self, angle)
        elif(axis == 1):
            Psolid_body.Ry(self, angle)
        elif(axis == 2):
            Psolid_body.Rz(self, angle)
        else:
            print("INVALID AXIS")
        return

    #rotating about x-axis
    @staticmethod
    def Rx(self, angle):
        for i in range(0,len(self.stuck_particles)):
              #getting attributes from object
              x0 = getattr(self.stuck_particles[i], 'x')
              y0 = getattr(self.stuck_particles[i], 'y')
              z0 = getattr(self.stuck_particles[i], 'z')
              
              #x rotation
              x1 = x0
              y1 = y0*np.cos(angle)-z0*np.sin(angle)
              z1 = y0*np.sin(angle)+z0*np.cos(angle)
              
              #setting particle attributes to rotated values
              setattr(self.stuck_particles[i], 'x', x1)
              setattr(self.stuck_particles[i], 'y', y1)
              setattr(self.stuck_particles[i], 'y', z1)
              
        return
            
    #rotating about y-axis
    @staticmethod
    def Ry(self, angle):
        for i in range(0, len(self.stuck_particles)):
            #getting attributes from object
            x0 = getattr(self.stuck_particles[i], 'x')
            y0 = getattr(self.stuck_particles[i], 'y')
            z0 = getattr(self.stuck_particles[i], 'z')

            #y rotation
            x1 = z0*np.sin(angle)+x0*np.cos(angle)
            y1 = y0
            z1 = z0*np.cos(angle)-x0*np.sin(angle)

            #setting particle attributes to rotated values
            setattr(self.stuck_particles[i], 'x', x1)
            setattr(self.stuck_particles[i], 'y', y1)
            setattr(self.stuck_particles[i], 'z', z1)

        return
      
    #rotating about z-axis
    @staticmethod
    def Rz(self, angle):
        for i in range(0, len(self.stuck_particles)):
            #getting attributes from object
            x0 = getattr(self.stuck_particles[i], 'x')
            y0 = getattr(self.stuck_particles[i], 'y')
            z0 = getattr(self.stuck_particles[i], 'z')

            #z rotation
            x1 = x0*np.cos(angle)-y0*np.sin(angle)
            y1 = x0*np.sin(angle)+y0*np.cos(angle)
            z1 = z0

            #setting particle attributes to rotated values
            setattr(self.stuck_particles[i], 'x', x1)
            setattr(self.stuck_particles[i], 'y', y1)
            setattr(self.stuck_particles[i], 'z', z1)
        return
