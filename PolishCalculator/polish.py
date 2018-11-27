#+, - (both unary and binary), *, /, ** over integers and floats, or, and and not over booleans
# At least a space ends each operands and operators, T and F respectively represent True and False.

import re
from stack import Stack
import math
class PolishCalculator:
     def __init__(self):
         self.evaluations = {'F': lambda : False, 'T': lambda :True, \
                            '-':lambda: float(-self.operands.pop())+float(self.operands.pop()), \
                            '+':lambda: float(self.operands.pop())+float(self.operands.pop()), \
                            '*':lambda: float(self.operands.pop())*float(self.operands.pop()), \
                            '/':lambda: math.divmod(tuple(reversed(list(float(self.operands.pop()),float(self.operands.pop())))))[0], \
                            '**':lambda: math.pow(tuple(reversed(list(float(self.operand.pop()),float(self.operand.pop()))))), \
                            'and':lambda: self.operands.pop() and self.operands.pop(), \
                            'or':lambda: self.operands.pop() or self.operands.pop(), \
                            'not':lambda: not(self.operands.pop())}
         self.operands = Stack()

     def __str__(self):pass

     def eval(self, expr):
        elements = re.sub('\s+',' ',expr).split(' ')
        for elem in elements:
            if elem in self.evaluations:
                self.operands+=self.evaluations[elem]()
            else:
                self.operands+=elem
        return str(self.operands.pop())


if __name__=='__main__':
    polish = PolishCalculator()
    print(polish.eval("1 2 + 3 * 4 +"))
    print(polish.eval("F not"))
