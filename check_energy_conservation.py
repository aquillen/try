# This is a static function file for
# chekcing energy conservation of the partical.
# Jeremy Kong

import numpy as np

from constants import *  # relevant constants!
from particle import *   # free particle class def and some routines
from solid_body import *  # solid body (Pan) routines
from free_particle_forces import *  # routines for calculating accelerations on free particles

# We are looking at E/m
# This sub-routine returns E/m
def get_E (particle,solid_body):
    return (get_KE(particle) + get_PE(particle) + get_L_npan(particle,solid_body))


# This sub-routine returns KE/m
def get_KE(particle):
    vsq = particle.vx ** 2 + particle.vy ** 2 + particle.vz **2 # v^2
    return 0.5 * vsq


# this sub-routine returns PE/M
def get_PE(particle):
    r = particle.y + Semi_major_Pan
    return -(G * mass_Saturn / r) # PE is negative


# this sub-routine return (L*n-pan)/m
def get_L_npan(particle,solid_body):
    n = len(solid_body.stuck_particles)  # number of stuck particle in solid_body
    sum = 0
    for i in range(0,n):  # loop over list of particles in the solid_body
        Gm_stuck_i = (G * solid_body.stuck_particles[i].mass)
        delta_x = np.abs(particle.x - solid_body.stuck_particles[i].x)
        sum += Gm_stuck_i/delta_x
    return -sum  # negative