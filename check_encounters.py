import particle   # free particle class def and some routines
import solid_body   # solid body (Pan) routines
import numpy as np


def is_collision(stuck_part, free_part):
    r_stuck = stuck_part.radius   # assign location params for x, y, z, r from stuck and free parts
    x_stuck = stuck_part.x
    y_stuck = stuck_part.y
    z_stuck = stuck_part.z
    r_free = free_part.radius
    x_free = free_part.x
    y_free = free_part.y
    z_free = free_part.z
    mass = free_part.mass

    # find distance between particles
    distance = np.sqrt((x_stuck - x_free) ** 2 + (y_stuck - y_free) ** 2 + (z_stuck - z_free) ** 2)
    if r_stuck + r_free >= distance:   # condition for free part to become stuck
        print('yes')
    else:
        print('no')


