from distutils.core import setup
from Cython.Build import cythonize

import numpy 

setup(
    name="quasi",
    version="0.0.1",
    description="Distributions for Quasi-Monte Carlo",
    author="abenton",
    author_email="andrew.reed.benton@gmail.com",
    license="MIT",
    packages=["quasi"],
    install_requires=[
        "scipy",
        "numpy",
        "cython"
    ],
    ext_modules = cythonize(["quasi/engines.pyx"]),
    include_dirs = [numpy.get_include()]
)
