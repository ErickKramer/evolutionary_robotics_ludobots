import numpy as np
from robot import ROBOT
import pyrosim
class INDIVIDUAL:
    def __init__(self):
        self.genome = np.random.rand()*2 - 1.0
        self.fitness = 0

    def evaluate(self):
        sim = pyrosim.Simulator(play_paused=False,
                                eval_time=500,
                                window_size=(1900, 1080))
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