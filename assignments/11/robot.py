import pyrosim
import numpy as np
import constants as c
import random
'''
Instructions:
https://www.reddit.com/r/ludobots/wiki/pyrosim/refactoring
'''
class ROBOT:
    def __init__(self, sim, wts):

        self.objects = {}
        self.joints = {}
        self.sensors = {}
        self.sensorNeurons = {}
        self.motorNeurons = {}

        self.send_objects(sim)
        self.send_joints(sim)
        self.send_sensors(sim)
        self.send_neurons(sim)
        self.send_synapses(sim, wts)

    def send_objects(self, sim):
        self.object_0 = sim.send_box(x=0,
                                     y=0,
                                     z=c.L + c.R,
                                     length=c.L,
                                     width=c.L,
                                     height=2*c.R,
                                     r=0.5,
                                     g=0.5,
                                     b=0.5)

        self.object_1 = sim.send_cylinder(x=0,
                                          y=c.L,
                                          z=c.L + c.R,
                                          length=c.L,
                                          radius=c.R,
                                          r=0.5,
                                          g=0.,
                                          b=0.,
                                          r1=0,
                                          r2=1,
                                          r3=0.)

        self.object_2 = sim.send_cylinder(x=c.L,
                                          y=0,
                                          z=c.L + c.R,
                                          length=c.L,
                                          radius=c.R,
                                          r=0.,
                                          g=0.5,
                                          b=0.,
                                          r1=1,
                                          r2=0,
                                          r3=0.)

        self.object_3 = sim.send_cylinder(x=0,
                                          y=-c.L,
                                          z=c.L + c.R,
                                          length=c.L,
                                          radius=c.R,
                                          r=0.,
                                          g=0.,
                                          b=0.5,
                                          r1=0,
                                          r2=-1,
                                          r3=0.)

        self.object_4 = sim.send_cylinder(x=-c.L,
                                          y=0,
                                          z=c.L + c.R,
                                          length=c.L,
                                          radius=c.R,
                                          r=0.25,
                                          g=0.,
                                          b=0.5,
                                          r1=-1,
                                          r2=0,
                                          r3=0.)

        self.object_5 = sim.send_cylinder(x=0,
                                          y=c.L/2 + c.L,
                                          z=c.L/2 + c.R,
                                          length=c.L,
                                          radius=c.R,
                                          r=1.,
                                          g=0.,
                                          b=0.)

        self.object_6 = sim.send_cylinder(x=c.L / 2 + c.L,
                                          y=0,
                                          z=c.L / 2 + c.R,
                                          length=c.L,
                                          radius=c.R,
                                          r=0.,
                                          g=1.,
                                          b=0.)

        self.object_7 = sim.send_cylinder(x=0,
                                          y=-(c.L / 2 + c.L),
                                          z=c.L / 2 + c.R,
                                          length=c.L,
                                          radius=c.R,
                                          r=0.,
                                          g=0.,
                                          b=1.)

        self.object_8 = sim.send_cylinder(x=-(c.L / 2 + c.L),
                                          y=0,
                                          z=c.L / 2 + c.R,
                                          length=c.L,
                                          radius=c.R,
                                          r=0.5,
                                          g=0.,
                                          b=1.)

        self.objects[0] = self.object_0
        self.objects[1] = self.object_1
        self.objects[2] = self.object_2
        self.objects[3] = self.object_3
        self.objects[4] = self.object_4
        self.objects[5] = self.object_5
        self.objects[6] = self.object_6
        self.objects[7] = self.object_7
        self.objects[8] = self.object_8

    def send_joints(self, sim):
        # Rotation through the yz plane using a normal vector of [-1.,0.,0.]
        # Rotation through the xz plane using a normal vector of [0.,-1.,0.]
        # The magnitude of the rotation does not affect much
        # Create a joint
        # Default range of rotation of the joints is +-pi/4 radians5
        # self.joint = sim.send_hinge_joint(first_body_id=self.blueObject,
        #                              second_body_id=self.redObject,
        #                              x=0.,
        #                              y=0.,
        #                              z=1.1,
        #                              n1=-1.,
        #                              n2=0.,
        #                              n3=0.,
        #                              lo=-np.math.pi / 2,
        #                              hi=np.math.pi / 2)

        self.joint_0 = sim.send_hinge_joint(first_body_id=self.object_0,
                                            second_body_id=self.object_1,
                                            x=0.,
                                            y=c.L/2,
                                            z=c.L+c.R,
                                            n1=-1.,
                                            n2=0.,
                                            n3=0.)

        self.joint_1 = sim.send_hinge_joint(first_body_id=self.object_1,
                                            second_body_id=self.object_5,
                                            x=0.,
                                            y=c.L/2 + c.L,
                                            z=c.L + c.R,
                                            n1=-1.,
                                            n2=0.,
                                            n3=0.)

        self.joint_2 = sim.send_hinge_joint(first_body_id=self.object_0,
                                            second_body_id=self.object_2,
                                            x=c.L/2,
                                            y=0.,
                                            z=c.L + c.R,
                                            n1=0.,
                                            n2=1.,
                                            n3=0.)

        self.joint_3 = sim.send_hinge_joint(first_body_id=self.object_2,
                                            second_body_id=self.object_6,
                                            x=c.L/2 + c.L,
                                            y=0.,
                                            z=c.L + c.R,
                                            n1=0.,
                                            n2=1.,
                                            n3=0.)

        self.joint_4 = sim.send_hinge_joint(first_body_id=self.object_0,
                                            second_body_id=self.object_3,
                                            x=0,
                                            y=-(c.L/2),
                                            z=c.L + c.R,
                                            n1=1.,
                                            n2=0.,
                                            n3=0.)

        self.joint_5 = sim.send_hinge_joint(first_body_id=self.object_3,
                                            second_body_id=self.object_7,
                                            x=0.,
                                            y=-(c.L/2 + c.L),
                                            z=c.L + c.R,
                                            n1=1.,
                                            n2=0.,
                                            n3=0.)

        self.joint_6 = sim.send_hinge_joint(first_body_id=self.object_0,
                                            second_body_id=self.object_4,
                                            x=-c.L/2,
                                            y=0.,
                                            z=c.L + c.R,
                                            n1=0.,
                                            n2=-1.,
                                            n3=0.)

        self.joint_7 = sim.send_hinge_joint(first_body_id=self.object_4,
                                            second_body_id=self.object_8,
                                            x=-(c.L/2 + c.L),
                                            y=0.,
                                            z=c.L + c.R,
                                            n1=0.,
                                            n2=-1.,
                                            n3=0.)

        self.joints[0] = self.joint_0
        self.joints[1] = self.joint_1
        self.joints[2] = self.joint_2
        self.joints[3] = self.joint_3
        self.joints[4] = self.joint_4
        self.joints[5] = self.joint_5
        self.joints[6] = self.joint_6
        self.joints[7] = self.joint_7

    def send_sensors(self, sim):
        # Create touch sensor
        # Sensor ignores connections between joints

        self.touch_0 = sim.send_touch_sensor(body_id=self.object_5)  # T0
        self.touch_1 = sim.send_touch_sensor(body_id=self.object_6)  # T1
        self.touch_2 = sim.send_touch_sensor(body_id=self.object_7)  # T2
        self.touch_3 = sim.send_touch_sensor(body_id=self.object_8)  # T3

        # Create a position sensor
        self.position_body = sim.send_position_sensor(body_id=self.object_0)  # P4

        # # Add a proprioceptive sensor
        # # This sensor returns the current angle of the joint
        # self.pro_1 = sim.send_proprioceptive_sensor(joint_id=self.joint)  # P2
        #
        # self.ray_1 = sim.send_ray_sensor(body_id=self.redObject,
        #                             x=0.,
        #                             y=0.5,
        #                             z=1.,
        #                             r1=0.,
        #                             r2=0.,
        #                             r3=-1.)  # R3

        self.sensors[0] = self.touch_0
        self.sensors[1] = self.touch_1
        self.sensors[2] = self.touch_2
        self.sensors[3] = self.touch_3

    def send_neurons(self, sim):
        for sensor_idx in self.sensors:
            self.sensorNeurons[sensor_idx] = sim.send_sensor_neuron(sensor_id=self.sensors[sensor_idx])

        for joint_idx in self.joints:
            self.motorNeurons[joint_idx] = sim.send_motor_neuron(joint_id=self.joints[joint_idx], tau=0.3)

    def send_synapses(self, sim, wts):
        for s in self.sensorNeurons:
            for m in self.motorNeurons:
                sim.send_synapse(source_neuron_id=self.sensorNeurons[s],
                                 target_neuron_id=self.motorNeurons[m],
                                 weight=wts[s, m])