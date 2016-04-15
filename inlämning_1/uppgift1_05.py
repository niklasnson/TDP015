from uppgift1_04 import *
import itertools

def satisfiable(expr):
    keys = set(expr.variables())
    possum = itertools.product([True,False], repeat=len(keys))
    for outer in possum:
        v = {}
        for inner in outer:
            for key in keys:
                v[key] = inner
        if expr.value(v):
            return v
    return False
