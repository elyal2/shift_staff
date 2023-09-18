import numpy
import random
from deap import base, creator, tools, algorithms
from functools import partial

# DEAP uses a dynamic approach to add methods to these objects, which can confuse static type checkers. 
# However, this doesn't mean that your code is incorrect. 
# If code runs without any runtime errors, we can safely ignore these warnings.
class GeneticScheduler:
    def __init__(self, num_employees, num_jobs):
        self.num_employees = num_employees
        self.num_jobs = num_jobs

        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMin) # type: ignore

        self.toolbox = base.Toolbox()
        self.toolbox.register("individual", self.init_individual)  
        self.toolbox.register("population", self.init_population)  # type: ignore

        self.toolbox.register("evaluate", self.cost)
        self.toolbox.register("mate", tools.cxTwoPoint)
        self.toolbox.register("mutate", self.mutate)
        self.toolbox.register("select", tools.selTournament, tournsize=3)

    def attr_int(self):
        return random.randint(0, self.num_employees-1)

    def init_individual(self):
        return creator.Individual([self.attr_int() for _ in range(self.num_jobs)]) # type: ignore

    def init_population(self, n):
        return [self.toolbox.individual() for _ in range(n)] # type: ignore

    def mutate(self, individual):
        return tools.mutUniformInt(individual, low=0, up=self.num_employees-1, indpb=0.1)

    def cost(self, individual):
        # This is a placeholder. You should implement this method based on your specific cost function.
        return sum(individual),

    def run(self, ngen=50, pop_size=100):
        pop = self.toolbox.population(n=pop_size) # type: ignore
        hof = tools.HallOfFame(1)
        stats = tools.Statistics(lambda ind: ind.fitness.values)
        stats.register("avg", numpy.mean)
        stats.register("min", numpy.min)
        stats.register("max", numpy.max)

        pop, logbook = algorithms.eaSimple(pop, self.toolbox, cxpb=0.5, mutpb=0.2, ngen=ngen, stats=stats, halloffame=hof, verbose=True)

        return pop, logbook, hof