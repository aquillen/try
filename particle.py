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
     
    #update position?
    #needs to also take in account other forces
    def update_pos(self, dt):
        self.x = self.vx*dt;
        self.y = self.vy*dt;
        self.z = self.vz*dt;
        self.vx = self.ax*dt;
        self.vy = self.ay*dt;
        self.vz = self.az*dt;

    
    #gets value of free from an existing object
    #returns boolean
    def is_stuck(obj):
        stuck = getattr(obj,'free')
        return stuck

