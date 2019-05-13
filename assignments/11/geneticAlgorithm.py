
import copy
import pickle
from population import POPULATION

'''
Instructions:
Implement a genetic algorithm
https://www.reddit.com/r/ludobots/wiki/pyrosim/geneticalgorithm

Blue diamond is the y coordinate
'''

save_best = True
visualize_best = True
num_generations = 200

# Initial population
parents = POPULATION(pop_size=5, blind_mode=True)
parents.create_population()

parents.evaluate()
print('Generation 0...')
parents.print_pop()

for gen in range(num_generations):
    children = POPULATION(pop_size=5, blind_mode=True)
    children.print_pop()
    exit()
#     children = copy.deepcopy(parents)
#     children.mutate()
#     children.evaluate()
#
#     parents.replace(children)
#     print('Generation ', gen+1, '...')
#     parents.print_pop()
#
# fittest_idx = parents.find_fittest()
#
# print('-----------------------------------------')
# print('The best individual found after {} generations is individual {} with a fitness of {}'\
#       .format(num_generations, fittest_idx, parents.p[fittest_idx].fitness))
# print('-----------------------------------------')
#
# if visualize_best:
#     parents.p[fittest_idx].start_evaluation(blind_mode=False)
#     parents.p[fittest_idx].compute_fitness()
#
# if save_best:
#     f = open('robot.p', 'wb')
#     pickle.dump(parents.p[fittest_idx], f)
#     f.close()