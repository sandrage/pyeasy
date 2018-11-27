from ABC import *
import types, inspect

class Stack:
    def __init__(self):
        self.elems = []
        self.end_calls = False
        fileopened = open("cg.dot",mode="w")
        fileopened.write("strict digraph cg { \n")
        fileopened.close()
    def push(self,elem):
        self.elems+=[elem]
        if(self.end_calls):
            self.end_calls = False
    def pop(self):
        fileopened = open("cg.dot",mode="a")
        if(not self.end_calls):
            self.end_calls = True
            fileopened.write(' -> '.join(self.elems))
            fileopened.write("\n")
        if len(self.elems) <= 2:
            fileopened.write("}")
        fileopened.close()
        return self.elems.pop()
    def flush(self):
        fileopened = open("cg.dot",mode="a")
        fileopened.write("}")
        fileopened.close()
def decorate_dot(funct,clsname):
    def wrapper(*args):
        global call_stack
        method_called = funct
        if inspect.currentframe().f_back.f_back is None:
            caller_method = "<main>"
            call_stack.push(caller_method)
        call_stack.push("{0}.{1}{2}".format(clsname,method_called.__name__,args))
        ret_value = funct(*args)
        call_stack.pop()
        return ret_value
    wrapper.func = funct
    return wrapper

class Dot(type):
    def __new__(metac,clsname,subs,dct):
        changed = []
        for attrname,attr in dct.items():
            if type(attr) is types.FunctionType:
                dct[attrname] = decorate_dot(attr,clsname)
                changed+=[dct[attrname]]
        cls = type.__new__(metac,clsname,subs,dct)
        for ch in changed:
            ch.func.__globals__[clsname]=cls
        return cls

A = Dot("A",(),dict(A.__dict__))
B = Dot("B",(),dict(B.__dict__))
C = Dot("C",(),dict(C.__dict__))
call_stack = Stack()
