import math

def pi_series():
    result = 0
    depth = 0
    den = 1
    while True:
        result += (4/den)*((-1)**depth)
        yield result
        depth+=1
        den+=2


def e_series():
    result = 0
    depth = 0
    while True:
        result += 1/math.factorial(depth)
        yield result
        depth+=1

def euler_accelerator(f):
    prev = next(f)
    current = next(f)
    succ = next(f)
    while True:
        result = succ - (((succ-current)**2)/(prev-(2*current)+succ))
        yield result
        prev = current
        current = succ
        succ = next(f)
