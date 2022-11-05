#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import os;
import sys;

os.chdir(os.path.dirname(__file__));
sys.path.insert(0, os.getcwd());

from src.thirdparty.maths import *;
from src.thirdparty.misc import *;
from src.models.quantum import *;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():
    q1 = random_qubit();
    q2 = Qubit(1, 0);
    print(dedent(
        f'''
        State: q1={q1:.3f}
        States after applying gates to q1:
        - X-Gate: {q1.x():.3f}
        - H-Gate: {q1.h():.3f}
        - Z-Gate: {q1.z():.3f}
        - measurement: {q1.m()}
        - Final state: {q1:.3f}

        State: q={q2:.3f}
        States after applying gates to q2:
        - H-Gate: {q2.h():.3f}
        - measurement: {q2.m()}
        - X-Gate: {q2.x():.3f}
        - Final state: {q2:.3f}
        '''
    ));
    return;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# EXECUTION
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
    main();
