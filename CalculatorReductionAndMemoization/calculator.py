class Expr:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def eval(self):pass

class Add(Expr):
    def __init__(self,first,second):
        super(Add,self).__init__(first,second)
        self.value = first.eval()+second.eval()
    def __str__(self):
        return "({0}+{1})".format(str(self.first),str(self.second))
    def eval(self):
        return self.value

class Sub(Expr):
    def __init__(self,first,second):
        super(Sub,self).__init__(first,second)
        self.value= first.eval()-second.eval()
    def __str__(self):
        return "({0}-{1})".format(str(self.first),str(self.second))
    def eval(self):
        return self.value

class Div(Expr):
    def __init__(self,first,second):
        super(Div,self).__init__(first,second)
        self.value = first.eval()//second.eval()
    def __str__(self):
        return "({0}/{1})".format(str(self.first),str(self.second))
    def eval(self):
        return self.value

class Mul(Expr):
    def __init__(self,first,second):
        super(Mul,self).__init__(first,second)
        self.value = first.eval() * second.eval()
    def __str__(self):
        return "({0}*{1})".format(str(self.first),str(self.second))

    def eval(self):
        return self.value
class Number(Expr):
    def __init__(self,value):
        self.value = int(value)
    def __str__(self):
        return "{0}".format(self.value)
    def eval(self):
        return self.value

class calculator:
    operations = {'+': lambda x,y: Add(x,y), '-': lambda x,y: Sub(x,y), '*': lambda x,y: Mul(x,y), '/':lambda x,y:Div(x,y)}
    def __init__(self,expr):
        self.expr=expr
    def print_reduction(self):
        def structure_creation(to_eval):
            if calculator.operations.get(to_eval[0]):
                (remaining,partial_result)=structure_creation(to_eval[1:])
                (last_remaining,second_result)=structure_creation(remaining)
                return last_remaining,calculator.operations[to_eval[0]](partial_result,second_result)
            return to_eval[1:],Number(to_eval[0])
        def eval(expr_to_eval):
            if isinstance(expr_to_eval,Number) or (isinstance(expr_to_eval.first,Number) and isinstance(expr_to_eval.second,Number)):
                return Number(expr_to_eval.eval())
            else:
                return expr_to_eval.__class__(eval(expr_to_eval.first), eval(expr_to_eval.second))
        def print_evaluation(expr_evaluated):
            print("{0}\n".format(str(expr_evaluated)))
            if not(isinstance(expr_evaluated,Number)):
                print_evaluation(eval(expr_evaluated))
            return expr_evaluated.eval()

        return print_evaluation(structure_creation(self.expr)[1])
