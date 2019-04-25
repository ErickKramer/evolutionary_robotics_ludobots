import random
import math
from robot import ROBOT
import pyrosim

class INDIVIDUAL:
    def __init__(self):
        self.genome = random.random()*2 - 1.0
        self.fitness = 0

    def evaluate(self,blind_mode=False):
        sim = pyrosim.Simulator(play_paused=False,
                                eval_time=1000,
                                window_size=(1900, 1080),
                                play_blind=blind_mode)
        robot = ROBOT(sim, self.genome)



        # Starts simulation
        sim.start()
        sim.wait_to_finish()

        # Position sensor returns [x,y,z] coordinates
        # svi 0 -> x
        # positionData_x = sim.get_sensor_data(sensor_id=robot.position_red, svi=0)
        positionData_y = sim.get_sensor_data(sensor_id=robot.position_red, svi=1)
        # positionData_z = sim.get_sensor_data(sensor_id=robot.position_red, svi=2)

        self.fitness = positionData_y[-1]

    def mutate(self):
        '''
        Generates a random value from a gaussian distribution centered to the value of self.genome
        random.gauss(mu, sigma)
        sigma is the absolute of the synaptic weight to allow search when the value is far from 0 and small search when close
        to zero
        '''
        self.genome = random.gauss(self.genome, math.fabs(self.genome))