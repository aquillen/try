# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

class particle:
    
    #constructor
    def __init__(self,mass,x,y,z,vx,vy,vg,v0,ax,ay,ag,free):
        self.mass = mass;
        self.x = x;
        self.y = y;
        self.z = z;
        self.vx = vx;
        self.vy = vy;
        self.vg = vg;
        self.v0 = v0;
        self.ax = ax;
        self.ay = ay;
        self.ag = ag;
        self.free = free;
        
    #update position?
    def update_pos(a, v, dt):
        dv = a*dt;
        dx = v* dt;
        return dv, dx

