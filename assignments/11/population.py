from individual import INDIVIDUAL

class POPULATION:
    def __init__(self, pop_size, blind_mode):
        self.p = {}
        self.pop_size = pop_size
        self.blind_mode = blind_mode

    def create_population(self):
        '''
        Creates a set of individuals
        '''
        for i in range(self.pop_size):
            self.p[i] = INDIVIDUAL(i)

    def print_pop(self):
        '''
        Displays the fitness of the individuals in the population
        '''
        for i in self.p:
            # self.p[i].print_genome()
            self.p[i].print_fitness()
        print()

    def evaluate(self):
        '''
        Starts a set of simulations in parallel and compute the fitness once they have finished running.
        '''
        for i in self.p:
            self.p[i].start_evaluation(blind_mode=self.blind_mode)

        for i in self.p:
            self.p[i].compute_fitness()

    def mutate(self):
        '''
        Mutate the genomes of the individuals in the population
        '''
        for i in self.p:
            self.p[i].mutate()

    def replace(self, other):
        '''
        :param other: population of individuals; (children)
        Replace the individuals in the population that have worst fitness with respect to the individuals
        in the "other" population
        '''

        assert len(self.p) == len(other.p), "Populations have different number of individuals"

        for i in self.p:
            if (self.p[i].fitness < other.p[i].fitness):
                self.p[i] = other.p[i]

    def find_fittest(self):
        '''
        Find the fittest individual in the population
        :return: index of the fittest individual
        '''
        fittest_idx = 0
        best_fitness = -9999
        for i in self.p:
            if self.p[i].fitness > best_fitness:
                best_fitness = self.p[i].fitness
                fittest_idx = i
        return fittest_idx