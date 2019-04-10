import pyrosim

# Creates simulation
'''
    Simulation starts in a pause state
    Ctrl+p unpause the simulation
    Ctrl+o advance step by step
'''
sim = pyrosim.Simulator(play_paused=True,
                        window_size=(1900,1080))

# Generates a cylinder with length of 1u and radius of 0.1u
# The ID of the object is stored in the variable whiteObject
'''
    Arguments:
    * Position (x,y,z)
    * Shape (length, radius)
    * Color (r,g,b)
    * orientation (r1,r2,r3)

'''
# rocketCylinder = sim.send_cylinder(x=2,
#                                    y=2,
#                                    z=0,
#                                    length=1.0,
#                                    radius=0.1,
#                                    r=0,
#                                    g=0,
#                                    b=1)

blueObject = sim.send_cylinder(x=0,
                               y=0,
                               z=0.6,
                               length=1.0,
                               radius=0.1,
                               r=0,
                               g=0,
                               b=1)
# Red object points into the screen
redObject = sim.send_cylinder(x=0,
                              y=0.5,
                              z=1.1,
                              length=1.0,
                              radius=0.1,
                              r=1,
                              g=0,
                              b=0,
                              r1=0,
                              r2=1,
                              r3=0)

# Generate a green cube
# greenBox = sim.send_box(x=3,
#                         y=3,
#                         z=0.5,
#                         mass=1.0,
#                         r1=1,
#                         r2=0,
#                         r3=0,
#                         length=1,
#                         width=1,
#                         height=1,
#                         collision_group='default',
#                         r=0,
#                         g=1,
#                         b=0)
#
# # Generate a sphere
# blackSphere = sim.send_sphere(x=3,
#                               y=3,
#                               z=1.5,
#                               r1=0,
#                               r2=0,
#                               r3=1,
#                               radius=0.5,
#                               mass=1.0,
#                               collision_group='default',
#                               r=0,
#                               g=0,
#                               b=0)

# Starts simulation
sim.start()
sim.wait_to_finish()
