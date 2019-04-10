import pyrosim
import numpy as np
import matplotlib.pyplot as plt

sim = pyrosim.Simulator(play_paused=False,
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

# Create touch sensor
# Sensor ignores connections between joints

touch_0 = sim.send_touch_sensor(body_id=blueObject)
touch_1 = sim.send_touch_sensor(body_id=redObject)

# Add a proprioceptive sensor
# This sensor returns the current angle of the joint
pro_1 = sim.send_proprioceptive_sensor(joint_id=joint)

print('=================================================')
# Starts simulation
sim.start()
sim.wait_to_finish()

# Recollect information of the first sensor
sensor_data_t0 = sim.get_sensor_data( sensor_id = touch_0 )
sensor_data_t1 = sim.get_sensor_data( sensor_id = touch_1 )
sensor_data_pro_1 = sim.get_sensor_data( sensor_id = pro_1 )

print('============================================================================')
print('Touch sensor for the blue cylinder')
print(sensor_data_t0)
print('============================================================================')
print('Touch sensor for the red cylinder')
print(sensor_data_t1)

# Plot sensors data
fig = plt.figure(figsize=(10,8))
ax1 = fig.add_subplot(311)
plt.plot(sensor_data_t0)
ax1.set_ylim(-1,+2)
ax1.set_title('Touch sensor blue cylinder')

ax2 = fig.add_subplot(312)
plt.plot(sensor_data_t1)
ax2.set_ylim(-1,+2)
ax2.set_title('Touch sensor red cylinder')

ax3 = fig.add_subplot(313)
plt.plot(sensor_data_pro_1)
ax3.set_title('Proprioceptive sensor in the joint')
plt.show()

#TODO: Pending from point 43 forwards from https://www.reddit.com/r/ludobots/wiki/pyrosim/sensors