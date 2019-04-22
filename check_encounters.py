from particle import *   # free particle class def and some routines
from solid_body import *  # solid body (Pan) routines
import numpy as np

def is_collision(stuck_part, free_part):
    r_stuck = stuck_part.r   # assign location params for x, y, z, r from stuck and free parts
    x_stuck = stuck_part.x
    y_stuck = stuck_part.y
    z_stuck = stuck_part.z
    r_free = free_part.r
    x_free = free_part.x
    y_free = free_part.y
    z_free = free_part.z
    distance = np.sqrt((x_stuck - x_free) ** 2 + (y_stuck - y_free) ** 2 + (z_stuck - z_free) ** 2)
    if r_stuck + r_free >= distance:   # condition for free part to become stuck
        # free_part now stuck

