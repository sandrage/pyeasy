import types
def case(expression):
    def wrapper(func):
        if type(expression) is list or type(expression) is tuple:
            func.cases=list(expression)
        else:
            func.cases = [expression]
        return func
    return wrapper
class Switch:
    def __init__(self):
        classdict = self.__class__.__dict__
        self.cases = {}
        for attrname,attr in classdict.items():
            if type(attr) is types.FunctionType and hasattr(attr,"cases"):
                self.cases[str(attr.cases)]=attr
    def match(self,expression):
        for expr,func in self.cases.items():
            if expression in eval(expr):
                return types.MethodType(func,self)
        for expr,func in self.cases.items():
            if 'default' in expr:
                return types.MethodType(func,self)
