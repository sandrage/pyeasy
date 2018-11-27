import random
import math

def divisors_of(n):
    #se n / i non da resto vuol dire che p divisibile
    return [i for i in range(2,int(math.sqrt(n))+1) if n%i == 0]

def trialdivision(p):
    print("Trial-Division's Primality Test", end="")
    #se p non ha divisori allora è primo
    return len(divisors_of(p))==0

def lucaslehmer(marsenne):
    print("Lucas Lehmers's Primality Test", end="")
    p = math.log2(marsenne+1)
    i = 0
    result = 4
    while i < p-2:
        result = (result * result) -2
        i+= 1
    return result % marsenne == 0

def littlefermat(p):
    print("Little Fermat's Primality Test", end="")
    random.seed()
    randomized = random.randrange(1,int(math.sqrt(p)))
    return 1 in [pow(random.randrange(1,p),p-1,p) for i in range(0,randomized)]

def is_prime(n):
    if n <= 10000:
        return trialdivision(n)
    elif n >= 10001 and n <= 524280:
        return lucaslehmer(n)
    else :
        return littlefermat(n)
