import numpy as np
from  constants import *
import particle
import solid_body

# Add Coriolis force onto acceleration vector of free particle
# n_Pan is defined in constants, this is the angular rotation rate, in frame moving with Pan
# Semi_major_Pan is in constants, is the semi-major axis of Pan
# coordinate system is such that Saturn is at (x,y,z) = (0,-Semi_major_Pan,0)
def Coriolis_force(particle):
    particle.ax += -2*n_Pan*particle.vy + n_Pan**2*particle.x
    particle.ay += 2*n_Pan*particle.vx + n_Pan**2*(particle.y + Semi_major_Pan)

# Add gravitational force from Saturn on to acceleration vector of free particle
def Saturn_force(particle):
    dy_Saturn = particle.y + Semi_major_Pan
    r_Saturn = np.sqrt(particle.x**2 + dy_Saturn**2 + particle.z**2 ) # distance to Saturn
    fac  = -G*mass_Saturn/r_Saturn**3
    particle.ax += fac * particle.x
    particle.ay += fac * dy_Saturn
    particle.az += fac * particle.z

# add gravitational forces from bound particles that belong to Pan onto free particle
# acceleration vector
def Pan_force(particle,solid_body):
    n = len(solid_body.stuck_particles)  # number of stuck particle in solid_body
    for i in range(0,n):  #loop over list of particles in the solid_body
        fac = -G*solid_body.stuck_particles[i].mass
        dx = particle.x - solid_body.stuck_particles[i].x  # vector between stuck and free particle
        dy = particle.y - solid_body.stuck_particles[i].y
        dz = particle.z - solid_body.stuck_particles[i].z
        rad = np.sqrt(dx**2 + dy**2 + dz**2)  # distance between stuck and free particle
        fac *= 1/rad**3
        particle.ax += fac*dx
        particle.ay += fac*dy
        particle.az += fac*dz

# compute all the forces on the particle after zeroing accelerations
def compute_forces(particle,solid_body):
    particle.zero_accel()
    # compute all forces
    Coriolis_force(particle)
    Saturn_force(particle)
    Pan_force(particle,solid_body)


# integrate with Eulerian integration a particle trajectory
def integrate_free(particle,solid_body,dt,nsteps):
    tvec = []
    xvec = []
    yvec = []
    zvec = []
#for i in range(0,nsteps):
# more here


