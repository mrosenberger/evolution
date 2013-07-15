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
        char_index = random.randint(2, len(self.content) - 2)
        return (self.content[:char_index - 1] + 
                random.choice('abcdefghijklmnopqrstuvwxyz') + self.content[char_index:])

class Environment:

    def __init__(self):
        pass

    def score(self, individual):
        return len(filter(lambda c:c=='a', individual.genome.content))

class Runner:

    def generate_children(self, individual, num):
        results = []
        for i in range(num):
            results.append(Individual(individual.genome.get_mutation()))
        return results

    def tick(self): # Sort by score, choose best, mutate, score mutations
        self.generations[-1].sort(key=lambda i:i.get_score())
        best = self.generations[-1][-self.skim_depth:]
        children = map(lambda i:generate_children(i, self.num_children))
        self.generations.append(sum(children, []))
        for child in self.generations[-1]:
            child.set_score(self.environment.score(child))
        
    def __init__(self, seed_individuals):
        self.environment = Environment()
        self.generation_size = 20 # Size of each generation
        self.skim_depth = 5 # How many of the top individuals we mutate from
        # Ensure that skim_depth is an even factor of generation_size
        self.num_children = self.generation_size / self.skim_depth
        self.generations = []
        self.generations.append(seed_individuals)

    def run(self, iterations):
        for i in range(iterations):
            self.tick()
        
