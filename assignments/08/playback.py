from individual import INDIVIDUAL
import pickle

f = open('robot.p', 'rb')
best = pickle.load(f)
f.close()

best.evaluate(blind_mode=False)
print('Fitness ', best.fitness)