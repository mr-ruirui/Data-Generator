
class Config:
    def __init__(self, pdf):
        self.iteration = 0
        self.pdf = pdf

    def read_config(self, parameters_txt):
        config_file = open(parameters_txt, 'r', encoding='utf-8')
        config_txt = config_file.read().strip().split('\n')

        for line in config_txt:
            if line.startswith('#') or line is '':
                continue
            elif line.startswith('T'):
                self.iteration = int(line.split('=')[1])

            elif line.startswith('size'):
                self.size = int(line.split('=')[1])
            else:
                parameters = line.split(':')[1].split(',')
                # 二项分布随机变量
                if line.startswith('binomial'):
                    parameters = line.split(':')[1].split(',')
                    self.binomial_n = float(parameters[0].split('=')[1])
                    self.binomial_p = float(parameters[1].split('=')[1])

                elif line.startswith('exponential'):
                    self.exponential_scale = float(parameters[0].split('=')[1])

                elif line.startswith('poisson'):
                    self.poisson_lam = float(parameters[0].split('=')[1])

                elif line.startswith('chisquare'):
                    self.chisquare_df = float(parameters[0].split('=')[1])

                elif line.startswith('dirichlet'):
                    self.dirichlet_alpha = float(parameters[0].split('=')[1])

                elif line.startswith('geometric'):
                    self.geometric_p = float(parameters[0].split('=')[1])

                elif line.startswith('normal'):
                    self.normal_mean = float(parameters[0].split('=')[1])
                    self.normal_scale = float(parameters[1].split('=')[1])

                elif line.startswith('uniform'):
                    self.uniform_low = float(parameters[0].split('=')[1])
                    self.uniform_high = float(parameters[1].split('=')[1])

                elif line.startswith('wald'):
                    self.wald_mean = float(parameters[0].split('=')[1])
                    self.wald_scale = float(parameters[1].split('=')[1])

        config_file.close()
