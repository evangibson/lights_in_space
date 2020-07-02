# Import libraries

import numpy as np
import matplotlib.pyplot as plt
import warnings
import copy
import pandas as pd


class dna:
    """Makes up the components of a population"""
    def __init__(self,
                 chromosome_length=9,
                 number_of_genes=2,
                 upper_range=6,
                 lower_range=-6):
        self.L = chromosome_length
        self.G = number_of_genes
        self.b = upper_range
        self.a = lower_range

        self.full = None  # Stand in for the genome that can be instantiated in spawn or otherwise

        self.precision = (self.b - self.a) / ((2 ** self.L) - 1)  # Can be calculated up front to save function calling

        self.score = None

    def spawn(self):
        """Generates a new random set of chromosomes"""
        self.full = np.random.randint(2,  # Sets 0,1 binary randomization
                                      size=(self.G,
                                            self.L))  # creates chromosones of length L for the number of genes specified

    def bit_summation(self):
        """Performs left to right summations for each chromosome"""

        x = lambda b, i: b * (2 ** i)  # Calculator for single bit

        self.full_summations = dict()

        for ix in range(0, self.G):  # need to happen for every gene
            power_list = list()
            bitplaceholder = 0
            for g in self.full[ix]:  # Enter the bits in a gene
                power_list.append(x(g, bitplaceholder))
                bitplaceholder += 1

            self.full_summations.update({ix: sum(power_list)})

    def decode_chromosomes(self):
        """Generates decoded values for input into fitness function"""
        self.gene_decoded = dict()

        self.eval_values = list()

        for s in list(self.full_summations.keys()):
            de = self.full_summations[s] * self.precision + self.a

            # For advanced mapping and tracing
            self.gene_decoded.update({s: de})

            # For brute force evaluation using "evaluate"
            self.eval_values.append(de)

    def evaluate(self, evaluation_function):
        """Evaluation function should be passed as a lambda function that tolerates the decoded chromosome values"""
        #  Arguments will be passed to eval function from left to right. Fitness function will need to index a list
        self.fitness = evaluation_function(self.eval_values)

    def mutate(self,
               chromosome_to_call,
               bit_to_flip):
        """Flips a bit to it's opposite. Will not determine randomness of procedure"""
        if self.full[chromosome_to_call][bit_to_flip] == 0:
            self.full[chromosome_to_call][bit_to_flip] = 1
        else:
            self.full[chromosome_to_call][bit_to_flip] = 0


class population:
    """Container for dna objects"""
    def __init__(self,
                 fitness_function,  # A lambda function that tolerates length G
                 dictionary_of_dna_objects=None,
                 # pass an existing population of dna objects if you don't want to generate a new one
                 start_index=None,
                 max_pop_size=100,  # can be set to the length of the dictionary of_dna_objects that are passed
                 **kwargs):  # used to pass dna argument

        if start_index is None:
            self.start = 0
        else:
            self.start = start_index

        if dictionary_of_dna_objects is None:
            print("Generate new population of size {}".format(max_pop_size))

            self.pool = dict()
            for i in range(self.start, self.start + max_pop_size):
                try:
                    temp_member = dna(**kwargs)

                except:
                    warnings.warn("Problem instantiating dna child objects. Reverting to default parameters")
                    temp_member = dna()

                # Stabilize DNA
                temp_member.spawn()
                temp_member.bit_summation()
                temp_member.decode_chromosomes()
                temp_member.evaluate(fitness_function)

                # The ids of each random dna object will be the index of the range
                self.pool.update({i: temp_member})


        else:
            # Keep in mind, ID will have to be assigned if population not generated from scratch
            self.pool = dictionary_of_dna_objects

        # Children pool
        try:
            self.child1 = dna(**kwargs)
            self.child1.spawn()
            self.child1.bit_summation()
            self.child1.decode_chromosomes()
            self.child1.evaluate(fitness_function)

            self.child2 = dna(**kwargs)
            self.child2.spawn()
            self.child2.bit_summation()
            self.child2.decode_chromosomes()
            self.child1.evaluate(fitness_function)

        except:
            warnings.warn("Problem instantiating dna child objects. Reverting to default parameters")
            self.child1 = dna()
            self.child2 = dna()

        self.fit_func = fitness_function
        self.max_pop_size = max_pop_size

    def rank_population(self):
        """Pulls fitness values out of existing pool and casts to a dataframe"""
        # Generate ordered lists of fitness and ids
        ids = list()
        fits = list()
        for m in list(self.pool.keys()):
            fits.append(self.pool[m].fitness)
            ids.append(m)

        self.ranks = pd.DataFrame({"ID": ids, "Score": fits}).sort_values("Score")

        # Generate a ranking column
        self.ranks["Placement"] = self.ranks['Score'].rank()

        return self.ranks

    def determine_survival(self, clone_function):
        """The clone function will act against the variable rank for each member of the population.
        The function should a 0 or 1:
        1 - Survive
        0 - Did not survive to next generation"""
        self.ranks['Survive'] = self.ranks["Placement"].map(clone_function)

    def crossover_breed(self,
                        parent_1_id,
                        parent_2_id,
                        swap_range=None,
                        random_cutoff_point=False,
                        chromosomes_to_cross=False,  # If False, will crossover all during breeding
                        crossover_start_point=0,
                        crossover_end_point=3):

        """Produces children as objects. Does not replace any population members"""

        # For each child, instantiate it as a copy of a parent and then overwrite a part of the chromosome with the adjacent parent
        self.child1 = copy.deepcopy(self.pool[parent_1_id])
        self.child2 = copy.deepcopy(self.pool[parent_2_id])

        # Loops over all chromosomes in the parent at the same points
        if chromosomes_to_cross is False:
            for chrom_index in range(0, self.child1.G):  # Arbitrary selection param
                self.child1.full[chrom_index][crossover_start_point:crossover_end_point] = self.pool[parent_2_id].full[chrom_index][crossover_start_point:crossover_end_point]
                self.child2.full[chrom_index][crossover_start_point:crossover_end_point] = self.pool[parent_1_id].full[chrom_index][crossover_start_point:crossover_end_point]

            self.child1.bit_summation()
            self.child1.decode_chromosomes()
            self.child1.evaluate(self.fit_func)

            self.child2.bit_summation()
            self.child2.decode_chromosomes()
            self.child2.evaluate(self.fit_func)

        else:
            print("Breeding aborted.")
