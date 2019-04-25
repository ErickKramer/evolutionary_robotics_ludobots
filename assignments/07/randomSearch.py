
import numpy as np
import matplotlib.pyplot as plt

from individual import INDIVIDUAL

'''
Instructions:
Implement random search
https://www.reddit.com/r/ludobots/wiki/pyrosim/randomsearch

Blue diamond is the y coordinate
'''

plot_flag = True
fitness_robots = []

for i in range(5):
    individual = INDIVIDUAL()
    individual.evaluate()
    print('Robot {} traveled {}'.format(i, individual.fitness))
    fitness_robots.append(individual.fitness)

## Ploting the data
if plot_flag == True:
    # Plot sensors data
    fig = plt.figure(figsize=(14, 14))

    ax1 = fig.add_subplot(111)
    plt.plot(fitness_robots)
    # ax1.set_ylim(-1, +2)
    ax1.set_title('Fitness of multiple robots')
    plt.grid()
    plt.show()