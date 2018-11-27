from good_practice2 import EnforceOO
class A(metaclass=EnforceOO):
    def __init__(self, val1,val2,val3):
        self.a1 = val1
        self.a2 = val2
        self.a3 = val3

    def m_a(self,newval):
        try:
            self.ma1=newval
        except AssertionError as e:
            print(e)
        self.a1 = newval

class B(metaclass=EnforceOO):
    def __init__(self, val1,val2,val3):
        self.b1 = 24
        self.b_a1 = A(val1,val2,val3)
        try:
            self.b_a1.a4 = 50
        except AssertionError as e:
            print(e)

class C(metaclass=EnforceOO):
    def __init__(self, val1,val2,val3,val4):
        self.c1 = val4
        self.c_b1 = B(val1,val2,val3)
    def m_c(self):
        try:
            self.c_b1.b3 = 60
        except AssertionError as e:
            print(e)
