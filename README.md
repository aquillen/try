## Growing an equatorial ridge on Pan

Here is a code outline.

Create free and bound particle objects.

Free particle class:

data:
<ul>
<li> position x,y,z </li>
<li> velocity vx,vy,vz </li>
<li> acceleration ax,ay,az</li>
<li> mass m</li>
<li> radius r</li>
</ul>

functions on free particles:

<ul>
<li> update position and velocity after timestep dt </li>
<li>   compute gravitational forces on particle and update accelerations from those forces </li>
<li>  search for encounter with the rigid body </li>
<li>  If encounter takes place turn the free particle in to a bound particle and add it to the rigid body </li>
</ul>
  
Rigid particle class:

data:
<ul>
<li> position x,y,z </li>
<li>  mass m </li>
<li>  radius r </li>
</ul>
  
Rigid body:

  A set of rigid particles
  
Functions on the rigid body:
<ul>
<li>  rotate so that it is in a minimum energy tidal rotation state with Saturn</li>
<li>  Add a free particle to the rigid body </li>
</ul>
   
Run time initial conditions 
<ul>
<li>   Set up an initial spherical central core for Pan </li>
<li>   generate free particles </li>
</ul>
  
Run time Loop:
<ul>
  <li> update positions of free particles  </li>
   <li> check for encounters between free particles and rigid body, stick free particles onto rigid body  </li>
   <li> update rotation of rigid body  </li>
   <li> remove boring free particles that are wasting time  </li>
</ul>  
  
Free parameters:
<ul>
  <li>     mass of free particles   </li>
  <li>     density of free particles (sets radius)  </li>
   <li>    initial distribution of free particles  </li>
        - semi-major axis, eccentricity and inclination distributions  
   </ul>


# Units:  kg, m s

Needed for forces 
Saturn_mass =  5.683E26 # kg 

Semi_major_Pan = 133584.0E3 #km to m

G = 6.67408E−11  #units m^2 kg-1 s-2

# angular rotation rate of Pan in orbit, this gives our Coriolis force

n_Pan = np.sqrt(G*Saturn_mass/Semi_major_Pan**3) 
