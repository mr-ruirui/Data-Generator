# -*- coding: utf-8 -*-
"""
@Author KG Group
"""
import sys
import numpy
from Config import Config


class DataGenerator:
    def __init__(self, config):
        self.config = config

    def generate(self):
        time_series = list()
        if self.config.pdf == 'binomial':
            for i in range(self.config.iteration):
                data = numpy.random.binomial(self.config.binomial_n, self.config.binomial_p, self.config.size)
                time_series.append(data)

        elif self.config.pdf == 'exponential':
            for i in range(self.config.iteration):
                data = numpy.random.exponential(self.config.exponential_scale, self.config.size)
                time_series.append(data)

        elif self.config.pdf == 'poisson':
            for i in range(self.config.iteration):
                data = numpy.random.poisson(self.config.poisson_lam, self.config.size)
                time_series.append(data)

        elif self.config.pdf == 'chisquare':
            for i in range(self.config.iteration):
                data = numpy.random.chisquare(self.config.chisquare_df, self.config.size)
                time_series.append(data)

        elif self.config.pdf == 'dirichlet':
            for i in range(self.config.iteration):
                data = numpy.random.dirichlet(self.config.dirichlet_alpha, self.config.size)
                time_series.append(data)

        elif self.config.pdf == 'geometric':
            for i in range(self.config.iteration):
                data = numpy.random.geometric(self.config.geometric_p, self.config.size)
                time_series.append(data)

        elif self.config.pdf =='normal':
            for i in range(self.config.iteration):
                data = numpy.random.normal(self.config.normal_mean,self.config.normal_scale,self.config.size)
                time_series.append(data)

        elif self.config.pdf =='uniform':
            for i in range(self.config.iteration):
                data = numpy.random.uniform(self.config.uniform_low,self.config.uniform_high, self.config.size)
                time_series.append(data)

        elif self.config.pdf =='wald':
            for i in range(self.config.iteration):
                data = numpy.random.wald(self.config.wald_mean,self.config.wald_scale, self.config.size)
                time_series.append(data)

        return time_series


if __name__ == '__main__':
    if len(sys.argv) <3:
        print('Usage:Python DataGenerator.py parameter_file_name possibility_distribution_function\n')
        sys.exit(0)
    parameters_txt = sys.argv[1]
    pdf = sys.argv[2]

    config_reader = Config(pdf)
    config_reader.read_config(parameters_txt)

    data_generator = DataGenerator(config_reader)
    time_series = data_generator.generate()

    print(time_series)
