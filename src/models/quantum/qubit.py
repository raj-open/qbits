#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from __future__ import annotations;
from src.thirdparty.code import *;
from src.thirdparty.maths import *;
from src.thirdparty.types import *;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# EXPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__all__ = [
    'Qubit',
];

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CONSTANTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MACHINE_EPS = 0.5e-12;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Classes
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@dataclass
class QubitBasic:
    alpha: complex = field(default=1);
    beta: complex = field(default=0);

class Qubit(QubitBasic):
    '''
    Creates a representation of a single qubit
    and provides internal methods the perform gate operations.

    @inputs
    - `alpha` - <complex>
    - `beta` - <complex>

    NOTE: `|alpha|² + |beta|²` must equal `1`.
    '''

    '''
    INITIALISATION
    NOTE: ensure probabilities add to 1!
    '''
    def __init__(self, alpha: complex, beta: complex):
        super().__init__(alpha=alpha, beta=beta);
        p = abs(self.alpha)**2 + abs(self.beta)**2;
        assert abs(p - 1) < MACHINE_EPS, f'Inputs must define a unit vector! Recievd a vector with ‖·‖² = {p:.6f}';
        # p should be exactly 1, but iron out numerical errors, just in case:
        c = sqrt(p);
        self.alpha = self.alpha/c;
        self.beta = self.beta/c;

    '''
    MAGIC METHODS
    '''

    def __str__(self) -> str:
        return format(self, '');

    def __format__(self, spec) -> str:
        if self.alpha == 0:
            return f'{format(self.alpha, spec)}|0⟩';
        if self.beta == 0:
            return f'{format(self.beta, spec)}|0⟩';
        return f'{format(self.alpha, spec)}|0⟩ + {format(self.beta, spec)}|1⟩';

    '''
    GATES
    '''

    def x(self) -> Qubit:
        '''
        Pauli-X gate swaps the bases |0⟩ and |1⟩.
        '''
        self = Qubit(alpha=self.beta, beta=self.alpha);
        return self;

    def y(self) -> Qubit:
        '''
        Pauli-Y rotates the phases of |0⟩ and |1⟩ by 90° and –90° respectively and then swaps the bases.
        '''
        self = Qubit(alpha=-1j*self.beta, beta=1j*self.alpha);
        return self;

    def z(self) -> Qubit:
        '''
        Pauli-Z gate switches the sign of |1⟩.
        '''
        self = Qubit(alpha=self.alpha, beta=-self.beta);
        return self;

    def h(self) -> Qubit:
        '''
        Hadamard transforms basis states into equidistributed superpositions.
        '''
        c = 1/sqrt(2);
        self = Qubit(
            alpha = c*(self.alpha + self.beta),
            beta = c*(self.alpha - self.beta),
        );
        return self;

    def m(self) -> Literal[0] | Literal[1]:
        '''
        Performs a measurement returning a basis state.
        '''
        probs = (abs(self.alpha)**2, abs(self.beta)**2);
        bit = choices((0, 1), probs)[0];
        if bit == 0:
            self = Qubit(alpha=1, beta=0);
        else:
            self = Qubit(alpha=0, beta=1);
        return bit;
