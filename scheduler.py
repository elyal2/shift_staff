from operator import attrgetter
from random import random, randint, shuffle

class Scheduler:
    def __init__(self, employees, job_positions):
        self.employees = employees
        self.job_positions = job_positions

    def cost(self, schedule):
        # This is a placeholder. You should implement this method based on your specific cost function.
        return sum(len(employees) for employees in schedule.values())

    def modify_schedule(self, schedule):
        # This is a placeholder. You should implement this method to generate a new schedule from the current one.
        return schedule

    def get_neighbors(self, schedule):
        # This is a placeholder. You should implement this method to generate all neighbors of the current schedule.
        return [schedule]

    def acceptance_probability(self, current_cost, new_cost, T):
        # This is a placeholder. You should implement this method based on the acceptance probability function of simulated annealing.
        return 1 if new_cost < current_cost else 0

    def select_parents(self, population):
        # This is a placeholder. You should implement this method based on your specific selection function. the method simply returns the first two schedules in the population
        return population[:2]

    def crossover(self, parents):
        # This is a placeholder. You should implement this method based on your specific crossover function.
        # the method simply returns the parents without performing any crossover. You should replace this with your own implementation that performs crossover to generate offspring from the parents.
        return parents
    
    def mutate(self, offspring):
        # This is a placeholder. You should implement this method based on your specific mutation function.
        pass

    def replace_population(self, population, offspring):
        # This is a placeholder. You should implement this method based on your specific replacement function.
        population.append(offspring)
        return population

    def schedule(self):
        # Sort employees by absenteeism (lower is better)
        self.employees.sort(key=attrgetter('absenteeism'))
        print('Employees sorted by absenteeism:')
        for employee in self.employees:
            print(f'\t{employee.id} ({employee.absenteeism})')

        # Create a dictionary to store the schedule
        schedule = {}

        # Create a list to store employees who have been assigned to a job
        assigned_employees = []

        # Iterate over each job position
        for job in self.job_positions:
            print(f'Considering job {job.id}:')
            print(f'\tJob requirements: {", ".join(job.get_required_skills())}')
            # Iterate over each employee
            for employee in self.employees:
                print(f'\tChecking employee {employee.id}:')
                print(f'\t\tEmployee skills: {", ".join(employee.skills)}')
                print(f'\t\tEmployee shift availability: {employee.shift_availability}')
                # Check if the employee is suitable for the job and is available
                #if job.is_suitable_for_employee(employee) and employee.is_available(job.id):
                    #print(f'\t\t{employee.id} is suitable and available')
                if job.is_suitable_for_employee(employee):
                    print(f'\t\t{employee.id} is suitable')
                    # If the job is not in the schedule, add it
                    if job.id not in schedule:
                        schedule[job.id] = []
                    # Add the employee to the job in the schedule
                    schedule[job.id].append(employee.id)
                    print(f'\t\tAdded {employee.id} to job {job.id}')
                    # Add the employee to the list of assigned employees
                    assigned_employees.append(employee)
                    # Break the loop as the job is filled
                    break
            else:
                print(f'\tNo suitable employees found for job {job.id}')

        # Remove assigned employees from the list of available employees
        for employee in assigned_employees:
            self.employees.remove(employee)

        return schedule
    def simulated_annealing(self):
        # Initial solution
        current_schedule = self.schedule()
        current_cost = self.cost(current_schedule)
        # Parameters for simulated annealing
        T = 1.0
        T_min = 0.00001
        alpha = 0.9
        while T > T_min:
            i = 1
            while i <= 100:
                new_schedule = self.modify_schedule(current_schedule)
                new_cost = self.cost(new_schedule)
                ap = self.acceptance_probability(current_cost, new_cost, T)
                if ap > random():
                    current_schedule = new_schedule
                    current_cost = new_cost
                i += 1
            T = T*alpha
        return current_schedule
    
    def heuristic_search(self):
        # Initial solution
        current_schedule = self.schedule()
        current_cost = self.cost(current_schedule)

        while True:
            neighbors = self.get_neighbors(current_schedule)
            next_schedule = None
            next_cost =  float('inf')  # Initialize to a large number
            for neighbor in neighbors:
                cost = self.cost(neighbor)
                if next_schedule is None or cost < next_cost:
                    next_schedule = neighbor
                    next_cost = cost
            if next_cost >= current_cost:
                return current_schedule
            else:
                current_schedule = next_schedule
                current_cost = next_cost
    

    def genetic_algorithm(self):
        # Initial population
        population = [self.schedule() for _ in range(100)]
        for _ in range(100):
            # Selection
            parents = self.select_parents(population)
            # Crossover
            offspring = self.crossover(parents)
            # Mutation
            self.mutate(offspring)
            # Replacement
            population = self.replace_population(population, offspring)
        # Return the best individual from the final population
        return min(population, key=self.cost)


    