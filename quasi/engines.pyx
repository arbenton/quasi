import numpy as np
cimport numpy as np

cimport cython

from quasi import constants

@cython.cdivision(True)
cdef halton_step(int seed, int base):
    if base <= 0:
        raise ValueError("Base must be greater than nonzero.")
    cdef double f = 1
    cdef double r = 0
    cdef int i = seed
    while i > 0:
        f /= base
        r += f*(i % base)
        i //= base
    return r

@cython.boundscheck(False)
cdef halton_seq(int n, int seed, int base):
    cdef np.ndarray r = np.zeros(n, dtype=np.float64)
    for i in range(0, n):
        r[i] = halton_step(seed + i, base)
    return r

cdef class HaltonEngine:
    cdef int maxdim, seed
    cdef list base

    def __init__(self, int maxdim, int seed=1000):
        if maxdim > len(constants.primes):
            raise ValueError("HaltonEngine supports up to %d dimensions." % len(constants.primes))
        self.maxdim = maxdim
        self.base = constants.primes[:self.maxdim]
        self.seed = seed
    
    def random(self, ndim, nrep):
        cdef np.ndarray r
        
        if ndim > self.maxdim:
            raise ValueError("ndim exceeds maxdim")
        
        if ndim > nrep:
            raise UserWarning("nrep > ndim, consider reversing these arguments.")

        r = np.zeros((ndim, nrep), dtype=np.float64)
        for i in range(ndim):
            r[i, :] = halton_seq(nrep, self.seed, self.base[i])
        self.seed += nrep
        return r
        