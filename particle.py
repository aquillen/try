# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

class free_particle:
    
    #constructor
    def __init__(self,mass,radius,x,y,z,vx,vy,vg,ax,ay,ag):
        self.mass = mass;
        self.radius = radius;
        self.x = x;
        self.y = y;
        self.z = z;
        self.vx = vx;
        self.vy = vy;
        self.vg = vg;
        self.ax = ax;
        self.ay = ay;
        self.ag = ag;
     
    #update position and velocity with timestep dt
    def update_pos(self, dt):
        self.x = self.vx*dt;
        self.y = self.vy*dt;
        self.z = self.vz*dt;
        self.vx = self.ax*dt;
        self.vy = self.ay*dt;
        self.vz = self.az*dt;
    
    # zero the acceleration vector
    def zero_accel(self):
        self.ax = 0
        self.ay = 0
        self.az = 0
    
    

