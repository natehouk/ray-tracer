from math import isnan

# Equality precision
EPSILON = 0.0001

# Recursion depth limit
LIMIT = 4


def equals(a, b):
    return abs(a - b) < EPSILON or (isnan(a) and isnan(b))
