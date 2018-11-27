from ABC import *
from good_practice2 import *

if __name__=='__main__':
    a = A(10,20,30)
    print("a : {0} \n \n".format(a))
    b = B(40,50,70)
    print("b: {0} \n \n ".format(b))
    c = C(80,90,100,110)
    print("c: {0}".format(c))
    try:
        c.v1 = 70
    except AssertionError as e:
        print(e)
