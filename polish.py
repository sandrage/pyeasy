from stack import Stack
import re
class ExpressionNotValidException(ValueError):pass

class PolishCalculator:
    def __init__(self):
        self.results = Stack()
        self.operators = ["+","*","/","**","and","or"]
        self.unaryOp = ["not","-"]
    def __str__(self):
        elems = self.expr.split(' ')
        try:
            for elem in elems:
                subExpr=elem
                if self.operators.count(elem)>0:
                    (secondOp, firstOp) = (self.results.pop(), self.results.pop())
                    subExpr = "({0}{1}{2})".format(firstOp,elem,secondOp)
                if self.unaryOp.count(elem)>0:
                    secondOp = self.results.pop()
                    firstOp = self.try_to_get_another_operand()
                    subExpr="({0}{1}{2})".format(firstOp, elem,secondOp)
                self.results.push(subExpr)
            return self.results.pop()
        except:
            raise ExpressionNotValidException()
    def try_to_get_another_operand(self):
        try:
            firstOp = self.results.pop()
        except IndexError:
            firstOp = ""
        return firstOp
    def eval(self,expr):
        self.expr=expr
        return eval(str(self).replace("T","True").replace("F","False"))


if __name__=='__main__':
    calc = PolishCalculator()
    print(calc.eval("2 3 + 5 *"))
    print(calc)
    print(calc.eval("2 3 -"))
    print("3 2 * - = {0}".format(calc.eval("3 2 * -")))
    print("15 7 1 1 + - / 3 * 2 1 1 + + - = {0}".format(calc.eval("15 7 1 1 + - / 3 * 2 1 1 + + -")))
