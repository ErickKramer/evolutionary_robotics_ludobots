import random
import math
from robot import ROBOT
import pyrosim
import numpy as np

class INDIVIDUAL:
    def __init__(self, id):
        # self.genome = random.random()*2 - 1.0
        self.genome = np.random.random(4)*2 - 1.0
        self.fitness = 0
        self.id = id

    def start_evaluation(self, blind_mode=False):
        '''
        :param blind_mode: Flag to disable the visualization

        Creates an instance of pyrosim and ROBOT
        '''
        self.sim = pyrosim.Simulator(play_paused=False,
                                eval_time=1000,
                                window_size=(1900, 1080),
                                play_blind=blind_mode)
        self.robot = ROBOT(self.sim, self.genome)

        self.sim.start()

    def compute_fitness(self):
        '''
        Waits for the simulation to finish, recollect the sensor data, and compute the fitness based
        on the distance traveled by the robot with respect to the y-axis
        '''
        self.sim.wait_to_finish()
        # Position sensor returns [x,y,z] coordinates
        # svi 0 -> x
        # positionData_x = sim.get_sensor_data(sensor_id=robot.position_red, svi=0)
        positionData_y = self.sim.get_sensor_data(sensor_id=self.robot.position_red, svi=1)
        # positionData_z = sim.get_sensor_data(sensor_id=robot.position_red, svi=2)

        self.fitness = positionData_y[-1]

        del self.sim

    def mutate(self):
        '''
        Generates a random value from a gaussian distribution centered to the value of self.genome
        random.gauss(mu, sigma)
        sigma is the absolute of the synaptic weight to allow search when the value is far from 0 and small search when close
        to zero
        '''

        gene_to_mutate = np.random.randint(0, 4) # Randomly choose the gene to mutate
        self.genome[gene_to_mutate] = random.gauss(self.genome[gene_to_mutate],
                                                   math.fabs(self.genome[gene_to_mutate]))

    def print_genome(self):
        print(self.genome)

    def print_fitness(self):
        print('[ID:{} - f:{}] '.format(self.id, self.fitness), end='')