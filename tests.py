import unittest

import numpy as np

from quasi.engines import HaltonEngine

class TestHaltonEngine(unittest.TestCase):
    """ Tests for HaltonEngine Class """

    def test_random_to_halton2(self):
        """ Compares to Known Halton(2) Sequence """
        halton = HaltonEngine(1, 1)
        aa = halton.random(1, 8)
        self.assertEqual(aa.shape, (1, 8))
        bb = np.array([[1/2, 1/4, 3/4, 1/8, 5/8, 3/8, 7/8, 1/16]])
        error = np.max(np.abs(aa - bb))
        self.assertLess(error, 1e-6)

if __name__ == "__main__":
    unittest.main()