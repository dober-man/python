#!/usr/bin/env python
__author__ = 'bradhscherer'
def digit_sum(n):
    total=0
    for char in str(n):
        total+=int(char)
    return total
