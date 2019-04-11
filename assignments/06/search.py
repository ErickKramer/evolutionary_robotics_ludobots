import pyrosim
import numpy as np
import matplotlib.pyplot as plt
from robot import ROBOT

'''
Instructions:
Robot with 10 random behaviours due to changes in the weight controlling the amount of influence between the touch 
sensor in the red cylinder and the motor in the joint.
https://www.reddit.com/r/ludobots/wiki/pyrosim/refactoring
'''

for i in range(10):
    sim = pyrosim.Simulator(play_paused=False,
                            eval_time=1000,
                            window_size=(1900, 1080))

    wt = np.random.rand()*2 - 1.0
    print(' Simulation {} with synapse weight of {}'.format(i, wt))
    robot = ROBOT(sim, wt)



    # Starts simulation
    sim.start()
    sim.wait_to_finish()
