import numpy as np
from scipy import special

from quasi.engines import HaltonEngine

class Generator(object):

    def _parse_size(self, size):
        if size is None:
            return 1, 1
        elif isinstance(size, int):
            n = size
            return 1, n
        elif isinstance(size, tuple):
            if len(size) == 1:
                n, = size
                return 1, n
            elif len(size) == 2:
                n, m = size
                return n, m
            else:
                raise ValueError("3D low discrepancy sequences are not supported")
        else:
            raise ValueError("size not understood")

    def uniform(self, low=0.0, high=1.0, size=None):
        """Simulate uniform variates"""
        n, m = self._parse_size(size)
        U = self.engine.random(n, m)
        return U

    def normal(self, loc=0.0, scale=1.0, size=None):
        """Simulate normal variates"""
        U = self.uniform(0, 1, size)
        X = scale*special.ndtri(U) + loc
        return X

    def lognormal(self, loc=0.0, scale=1.0, size=None):
        """ Simulate lognormal variates"""
        Y = self.normal(loc, scale, size)
        X = np.exp(Y)
        return X 

    def exponential(self, scale=1.0, size=None):
        """ Simulate exponential variates"""
        U = self.uniform(0, 1, size)
        X = -scale*np.log(U)
        return X

    def weibull(self, a, size=None):
        """ Simulate weibull variates """
        U = self.uniform(0, 1, size)
        X = (-np.log(U))**(1/a)
        return X

    def gamma(self, shape, scale=1.0, size=None):
        """ simulate Gamma variates """
        U = self.uniform(0, 1, size)
        X = special.gdtrix(1/scale, shape, U)
        return X

    def multivariate_normal(self, mean, cov, size=None):
        Z = self.normal(0, 1, size=size)
        X = mean + cov.dot(Z)
        return X

class Halton(Generator):
    def __init__(self, maxdim=50, seed=100):
        if maxdim > 50:
            raise ValueError("High dimensional Halton sequences have high correlation - recommend another method.")
        self.maxdim = maxdim
        self.engine = HaltonEngine(maxdim)

