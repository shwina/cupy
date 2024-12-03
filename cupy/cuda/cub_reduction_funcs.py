# numba doesn't like callables defined inside `.pyx`
# files (they have type `cyfunction`).
def add(x, y): return x + y
