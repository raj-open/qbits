#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from src.thirdparty.maths import *;
from src.models.quantum.qubit import *;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# EXPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__all__ = [
    'random_qubit',
];

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Methods
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def random_qubit() -> Qubit:
    '''
    Generates a random qubit.
    '''
    theta = uniform(0, 2*pi);
    phi1 = uniform(0, 2*pi);
    phi2 = uniform(0, 2*pi);
    z1 = cos(phi1) + 1j*sin(phi1);
    z2 = cos(phi2) + 1j*sin(phi2);
    # create random normalised coefficients:
    alpha = z1*cos(theta);
    beta = z2*sin(theta);
    return Qubit(alpha=alpha, beta=beta);
