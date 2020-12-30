# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 23:10:17 2020

@author: Daniel
"""

from homework1 import is_prime
from homework1 import add_frac

def test_is_prime():
    assert is_prime(12) == True
 
def test_add_frac():
    assert add_frac(12,34,24,65) == 'Ergebnis ungekürzt: 12/34 + 24/65 = 1596/2210'

