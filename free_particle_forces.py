import numpy as numpy
import constants
import particle
import solid_body

# Add coriolis force onto acceleration vector of free particle
# n_Pan is defined in constants
def coriolis_force(particle):
    particle.ax += n_Pan*particle.vy
    particle.ay += n_Pan*particle.vx


# Add gravitational force from Saturn on to acceleration vector of free particle
def Saturn_force(particle):
    particle.ax += G*mass_Saturn

# add gravitational forces from bound particles that belong to Pan onto free particle
# acceleration vector
def Pan_force(particle,solid_body):
    n = len(solid_body.stuck_particles)
    for i in range(0,n):
        particle.ax += 0
        particle.ay += 0
        particle.az += 0
