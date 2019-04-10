import pyrosim
import numpy as np

sim = pyrosim.Simulator(play_paused=True,
                        window_size=(1900,1080))

blueObject = sim.send_cylinder(x=0.,
                               y=0.,
                               z=0.6,
                               length=1.,
                               radius=0.1,
                               r=0.,
                               g=0.,
                               b=1.)
# Point towards the red marker [0.5, 0., 1.1] r = [1., 0., 0.]
# Point towards the blue marker [0., 0.5, 1.1] r = [0., 1., 0.]
redObject = sim.send_cylinder(x=0.,
                              y=0.5,
                              z=1.1,
                              length=1.,
                              radius=0.1,
                              r=1,
                              g=0.,
                              b=0.,
                              r1=0.,
                              r2=1.,
                              r3=0.)
# Rotation through the yz plane using a normal vector of [-1.,0.,0.]
# Rotation through the xz plane using a normal vector of [0.,-1.,0.]
# The magnitude of the rotation does not affect much
# Create a joint
# Default range of rotation of the joints is +-pi/4 radians5
joint = sim.send_hinge_joint(first_body_id=blueObject,
                             second_body_id=redObject,
                             x=0.,
                             y=0.,
                             z=1.1,
                             n1=-1.,
                             n2=0.,
                             n3=0.,
                             lo=-np.math.pi/2,
                             hi=np.math.pi/2
                             )

# Starts simulation
sim.start()
sim.wait_to_finish()
