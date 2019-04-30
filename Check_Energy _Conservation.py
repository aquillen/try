# This is a static function file for
# chekcing energy conservation of the partical.
# Jeremy Kong

import numpy as np

from constants import *  # relevant constants!
from particle import *   # free particle class def and some routines
from solid_body import *  # solid body (Pan) routines
from free_particle_forces import *  # routines for calculating accelerations on free particles

def check_energy(particle _p):
    #TODO