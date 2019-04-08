# Growing an equatorial ridge on Pan

Here is a code outline.

Create free and bound particle objects.


Free particle class:
data:
  position x,y,z
  velocity vx,vy,vz
  acceleration ax,ay,az
  mass m
  radius r
functions:
  -update position and velocity after timestep dt
  -compute gravitational forces on particle and update accelerations from those forces
  -search for encounter with the rigid body
  -If encounter takes place turn the free particle in to a bound particle and add it to the rigid body
  
Rigid particle class
data:
  position x,y,z
  mass m
  radius r
  
Rigid body:
  A set of rigid particles
functions:
  rotate so that it is in a minimum energy tidal rotation state with Saturn
  
  
Run time:
  Set up an initial spherical central core for Pan
  generate free particles
  
  Loop:
  -update positions of free particles
  -check for encounters between free particles and rigid body, stick free particles onto rigid body
  -update rotation of rigid body
  -remove boring free particles that are wasting time
  
  
  Free parameters:
    mass of free particles 
    density of free particles (sets radius)
    initial distribution of free particles
      - semi-major axis, eccentricity and inclination distributions

