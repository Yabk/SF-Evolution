"""Module containing Cartesian Genetic Programming model of an Individual"""
import random
from ..individual import Individual, IndividualGenerator
from .modules import *


class CGPGenerator(IndividualGenerator):
    """A CPG individual factory"""

    def __init__(self, input_len, grid_size, output_len,
                 modules=(module_sum, module_difference, module_product,
                          module_quotient, module_sine, module_cosine,
                          min, max)):
        """Initialize CPG hyperparameters"""
        super().__init__()
        self.input_len = input_len
        self.grid_size = grid_size
        self.output_len = output_len
        self.modules = modules

    def generate(self):
        """Generate a CGP individual"""
        return CGPIndividual(self.input_len, self.grid_size, self.output_len, self.modules)


class CGPIndividual(Individual):
    """A CGP individual"""

    def __init__(self, input_len, grid_size, output_len,
                 modules=(module_sum, module_difference, module_product,
                          module_quotient, module_sine, module_cosine,
                          min, max), chromosome=None):
        """Initialize CGPIndividual.

        :param input_len: number of inputs to the individual
        :param grid_size: tuple containing width and height of module grid
        :param output_len: number of outputs from the individual
        :param modules: list of functions - modules
        """
        super().__init__()

        self.input_len = input_len
        self.grid_width = grid_size[0]
        self.grid_height = grid_size[1]
        self.output_len = output_len
        self.modules = modules
        self.modules_len = len(modules)

        if chromosome is None:
            self.chromosome = [0] * (self.grid_width * self.grid_height * 3 + output_len)
            self.randomize()
        else:
            if not self.check_chromosome(chromosome, input_len, grid_size, output_len):
                raise ValueError('Invalid chromosome length ({}) for given individual dimensions'
                                 .format(len(chromosome)))
            self.chromosome = chromosome



    def evaluate(self, inputs):
        """Evaluate given inputs and return outputs"""
        if len(inputs) != self.input_len:
            raise ValueError('Bad input length for inputs {}, was expecting length {}.'
                             .format(inputs, self.input_len))

        module_outputs = {}
        for i, input_value in enumerate(inputs):
            module_outputs[i] = input_value

        # Find all the modules that need to be evaluated

        to_evaluate = []
        for output in self.chromosome[-self.output_len:]:
            if output >= self.input_len:
                to_evaluate.append(output)

        i = 0
        while i < len(to_evaluate):
            output_index = to_evaluate[i]
            module_index = self._module_index(output_index)
            module_dependencies = self.chromosome[module_index:module_index+2]
            for dependency in module_dependencies:
                if (dependency >= self.input_len) and (dependency not in to_evaluate):
                    to_evaluate.append(dependency)
            i += 1

        # Evaluate all modules that need to be evaluated

        to_evaluate.sort()

        for output_index in to_evaluate:
            module_index = self._module_index(output_index)
            input1 = module_outputs[self.chromosome[module_index + 0]]
            input2 = module_outputs[self.chromosome[module_index + 1]]
            module = self.modules[self.chromosome[module_index + 2]]

            module_outputs[output_index] = module(input1, input2)


        # Compose final outputs
        outputs = []
        for output in self.chromosome[-self.output_len:]:
            outputs.append(module_outputs[output])

        return outputs


    def to_file(self, file_path):
        """Export individual to a text file"""
        with open(file_path, 'w') as export_file:
            export_file.write(str(self.input_len)+' '+str(self.grid_width)+' '+
                              str(self.grid_height)+' '+str(self.output_len)+'\n')
            export_file.write(' '.join([module.__name__ for module in self.modules])+'\n')
            export_file.write(' '.join([str(v) for v in self.chromosome])+'\n')
            export_file.write(str(self.fitness))


    @staticmethod
    def from_file(file_path):
        """Import CGP individual from a text file"""
        with open(file_path, 'r') as import_file:
            lines = [line.rstrip() for line in import_file.readlines()]
        input_len, grid_width, grid_height, output_len = [int(v) for v in lines[0].split(' ')]
        modules = [eval(module) for module in lines[1].split(' ')]
        chromosome = [int(v) for v in lines[2].split(' ')]
        fitness = float(lines[3])

        cgp = CGPIndividual(input_len, (grid_width, grid_height),
                            output_len, modules=modules, chromosome=chromosome)
        cgp.fitness = fitness

        return cgp


    def randomize(self):
        """Randomize the chromosome of this individual"""
        # Randomize layer by layer ensuring we end up with a valid CGP individual
        for layer in range(self.grid_width):
            # len of allowed module inputs for this layer
            valid_input_len = self.input_len + layer * self.grid_height

            for module in range(self.grid_height):
                module_index = 3 * (self.grid_height * layer + module)
                self.chromosome[module_index + 0] = random.randrange(0, valid_input_len)
                self.chromosome[module_index + 1] = random.randrange(0, valid_input_len)
                self.chromosome[module_index + 2] = random.randrange(0, self.modules_len)

        # Randomize outputs
        valid_outputs_len = self.input_len + self.grid_width * self.grid_height
        size = self.grid_width * self.grid_height * 3 + self.output_len
        for i in range(size - self.output_len, size):
            self.chromosome[i] = random.randrange(0, valid_outputs_len)


    def _module_index(self, output_index):
        """Return index in chromosome array for module with given output_index"""
        if output_index < self.input_len:
            raise ValueError('Given index {} is input. Input length for given \
                    CGPIndividual is {}'.format(output_index, self.input_len))

        return (output_index - self.input_len) * 3


    @staticmethod
    def check_chromosome(chromosome, input_len, grid_size, output_len):
        """Check if length of chromosome is valid according to given individual dimensions"""
        return len(chromosome) == (grid_size[0] * grid_size[1] * 3) + output_len
