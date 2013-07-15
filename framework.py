#!/usr/bin/python

import random

class Individual:

    def __init__(self, genome):
        self.genome = genome
        self.score = None

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

class Genome:
    
    def __init__(self, content):
        self.content = content

    def get_mutation(self):
        char_index = random.randint(0, len(self.content) - 1)
        char = random.choice('abcdefghijklmnopqrstuvwxyz')
        listed = list(self.content)
        listed[char_index] = char
        return ''.join(map(str, listed))

class Environment:

    def __init__(self):
        pass

    def score(self, individual):
        return len(filter(lambda c:c=='b', individual.genome.content))

class Runner:

    def generate_children(self, individual, num):
        results = []
        for i in range(num):
            results.append(Individual(Genome(individual.genome.get_mutation())))
        return results

    def tick(self): # Sort by score, choose best, mutate, score mutations
        self.generations[-1].sort(key=lambda i:i.get_score())
        best = self.generations[-1][-self.skim_depth:]
        children = map(lambda i:self.generate_children(i, self.num_children), best)
        self.generations.append(sum(children, []))
        for child in self.generations[-1]:
            child.set_score(self.environment.score(child))

    def run(self, iterations):
        for i in range(iterations):
            self.tick()

    def generate_initial_individuals(self, num):
        individuals = []
        for i in range(num):
            genome = ''
            for j in range(10):
                genome += random.choice('abcdefghijklmnopqrstuvwxy')
            individuals.append(Individual(Genome(genome)))
        return individuals

    def __init__(self, generation_size=20, skim_depth=5, seed_individuals=None):
        self.environment = Environment()
        self.generation_size = generation_size # Size of each generation
        self.skim_depth = skim_depth # How many of the top individuals we mutate from (must be factor of generation_size)
        self.num_children = self.generation_size / self.skim_depth
        self.generations = []
        if seed_individuals:
            self.generations.append(seed_individuals)
        else:
            self.generations.append(self.generate_initial_individuals(self.generation_size))

r = Runner()
while (True):
    print('Individuals:')
    for individual in r.generations[-1]:
        print(individual.genome.content)
    raw_input()
    print('Ticking...')
    r.tick()
    print('Done')
