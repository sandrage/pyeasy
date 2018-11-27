
class mycomplex:
    def __init__(self,real,imm):
        self._real=real
        self._imm=imm
    def __add__(self,other):
        return mycomplex(self._real+other._real,self._imm+other._imm)
    def __radd__(self,other):
        return mycomplex(self._real+other,self._imm)
    def __sub__(self,other):
        return mycomplex(self._real-other._real,self._imm-other._imm)
    def __rsub__(self,other):
        return mycomplex(self._real-other,self._imm)
    def __mul__(self,other):
        return mycomplex((self._real*other._real)-(self._imm*other._imm), (self._imm*other._real)+(self._real*other._imm))
    def __rmul__(self,other):
        return mycomplex((self._real*other)-self._imm, (self._imm*other)+self._real)
    def __truediv__(self,other):
        realpart = ((self._real*other._real)+(self._imm*other._imm))/(other._real**2+other._imm**2)
        immpart = ((self._imm*other._real)-(self._real*other._imm))/(other._real**2+other._imm**2)
        return mycomplex(realpart,immpart)
    def __rtruediv__(self,other):
        realpart = ((self._real*other)+self._imm)/(other**2)
        immpart = ((self._imm*other)-self._real)/(other**2)
        return mycomplex(realpart,immpart)
    def __str__(self):
        real=""
        imm=""
        if type(self._real) is int and self._real!=0:
            real="{0: }".format(self._real)
        elif type(self._real) is float and self._real!=0.:
            real="{0: .2}".format(self._real)
        if type(self._imm) is int:
            if abs(self._imm)==1:
                imm=(self._imm>0 and "+" or "-")+("i".format(self._imm))
            else:
                imm="{0:+}i".format(self._imm)
        elif type(self._imm) is float:
            if abs(self._imm)==1.:
                imm=((self._imm>0.)and "+" or "-")+("i".format(self._imm))
            else:
                imm="{0:+.2}i".format(self._imm)

        return real+imm
