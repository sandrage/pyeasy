'''
sin(x) can be approximate by the Taylor's series:

x - x^3/3! + x^5/5! ...

Let's write a library to implement sin(x, n) by using the Taylor's series (where n is the level of approximation, i.e., 1 only one item, 2 two items, 3 three items and so on).

Let's compare your function with the one implemented in the math module at the growing of the approximation level.

Hint. Use a generator for the factorial and a comprehension for the series.
'''

import math

def factorial():
    res = 1
    increm = 1
    while True:
        yield res
        increm = increm + 1
        res = res * increm * (increm+1)
        increm = increm + 1



def taylorseries(x, n):
    fact = factorial()
    return math.fsum([math.pow(-1, l-1)*math.pow(x,2*l-1)/next(fact) for l in range(1,n+1) ])

print("Funzione sin ufficiale: {0}".format(math.sin(10)))
print("Serie di taylor: {0}".format(taylorseries(10,20)))