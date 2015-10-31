#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2011 ~ 2012 Deepin, Inc.
#               2011 ~ 2012 Wang Yong
# 
# Author:     Wang Yong <lazycat.manatee@gmail.com>
# Maintainer: Wang Yong <lazycat.manatee@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from numpy import matrix
from numpy import linalg

def solve_parabola((ax, ay), (bx, by), (cx, cy)):
    '''
    y = a * x ^ 2 + b * x + c

    three pointers: (-1, 7), (1, 15), (-2, 9)
    we got three equations:
       7  = a  - b  + c
       15 = a  + b  + c
       9  = 4a - 2b + c
    then matrix A is:
       [[1, -1, 1], [1, 1, 1], [4, -2, 1]]

    matrix X is:
       [a, b, c]

    matrix B is:
       [[7], [15], [9]]
       
    Because AX = B, if we want got X, we should use equation:
       X = inverse(A) * B
    '''
    matrix_a = matrix([[pow(ax, 2), ax, 1], [pow(bx, 2), bx, 1], [pow(cx, 2), cx, 1]])
    matrix_b = matrix([[ay], [by], [cy]])
    
    return linalg.solve(matrix_a, matrix_b).tolist()
