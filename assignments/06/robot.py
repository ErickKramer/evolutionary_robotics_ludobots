import pyrosim
import numpy as np

'''
Instructions: 
https://www.reddit.com/r/ludobots/wiki/pyrosim/refactoring
'''
class ROBOT:
    def __init__(self, sim, wt):
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
        #----------------------------------------------------------------------------------
        # Create touch sensor
        # Sensor ignores connections between joints

        touch_blue = sim.send_touch_sensor(body_id=blueObject)
        touch_red = sim.send_touch_sensor(body_id=redObject)

        # Add a proprioceptive sensor
        # This sensor returns the current angle of the joint
        pro_1 = sim.send_proprioceptive_sensor(joint_id=joint)

        ray_1 = sim.send_ray_sensor(body_id=redObject,
                                    x=0.,
                                    y=0.5,
                                    z=1.,
                                    r1=0.,
                                    r2=0.,
                                    r3=-1.)
        #----------------------------------------------------------------------------------
        # Adding neuron to capture the data coming from the touch sensors
        sensor_neuron_blue = sim.send_sensor_neuron(sensor_id=touch_blue)
        sensor_neuron_red = sim.send_sensor_neuron(sensor_id=touch_red)

        # Add motor neuron
        # Motor neurons are attached to joints and passes its value along
        # The motor neurons control the rotation of the joint
        # Motor neurons only takes values between -1 and 1
        motor_neuron_joint = sim.send_motor_neuron(joint_id=joint)

        # Create synapses
        # Synapses do not have id
        sim.send_synapse(source_neuron_id=sensor_neuron_red,
                         target_neuron_id=motor_neuron_joint,
                         weight=wt)

        # sim.send_synapse(source_neuron_id=sensor_neuron_blue,
        #                  target_neuron_id=motor_neuron_joint,
        #                  weight=0.)
