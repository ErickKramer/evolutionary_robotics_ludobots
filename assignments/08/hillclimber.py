
import copy
import matplotlib.pyplot as plt
import pickle
from individual import INDIVIDUAL

'''
Instructions:
Implement hill climber search
https://www.reddit.com/r/ludobots/wiki/pyrosim/hillclimber

Blue diamond is the y coordinate
'''

plot_flag = True
visualize_best = True
fitness_robots = []

parent = INDIVIDUAL()
parent.evaluate(blind_mode=False)
print(parent.fitness)
for i in range(100):
    child = copy.deepcopy(parent)
    child.mutate()
    child.evaluate(blind_mode=True)

    print('[g:{}] - [Pw:{}] - [P:{}] - [c:{}]'.format(i, parent.genome, parent.fitness, child.fitness))

    if (child.fitness > parent.fitness):
        parent = child
        fitness_robots.append(child.fitness)
        child.evaluate(blind_mode=True)

        # Save the strongest model
        f = open('robot.p', 'wb')
        pickle.dump(parent,f)
        f.close()
    else:
        fitness_robots.append(parent.fitness)

if visualize_best:
    parent.evaluate(blind_mode=False)

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