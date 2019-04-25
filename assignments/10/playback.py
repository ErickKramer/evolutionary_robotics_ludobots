from individual import INDIVIDUAL
import pickle

f = open('robot.p', 'rb')
best = pickle.load(f)
f.close()

best.start_evaluation(blind_mode=False)
best.compute_fitness()
print('Fitness ', best.fitness)