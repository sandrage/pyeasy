from inspect import *
from types import FunctionType
def DOTdecorator(f,classname):
    class decorator:
        def __init__(self):
            self.function=f
            self.classname=classname
            self.graph_state=""
        def __call__(self,*args):
            caller_name= currentframe().f_back.f_code.co_name
            #print("-----------{0} \n \n ".format(getouterframes(currentframe())))
            graph=open("cg.dot",mode='a')
            toflush=None
            if(caller_name=="<module>"):
                self.graph_state="strict digraph cg{\n"
                self.graph_state+="\t main -> \"{2}.{0}({1})\"".format(self.function.__name__,*args,self.classname)
            else:
                self_caller = currentframe().f_back.f_back.f_locals['self']
                self_caller.graph_state=self_caller.graph_state+" -> \"{2}.{0}({1})\"".format(self.function.__name__,*args,self.classname)
            result = self.function(*args)
            graph.write(self.graph_state)
            graph.close()
            return result
    return decorator()

class DotFunctions(type):
    def __new__(meta,classname,subs,diction):
        for (attr,value) in diction.items():
            if (isinstance(value,FunctionType)):
                diction[attr]=DOTdecorator(value,classname)
        return type.__new__(meta,classname,subs,diction)

import ABC
ABC.A=DotFunctions('A',(),dict(ABC.A.__dict__))
ABC.B=DotFunctions('B',(),dict(ABC.B.__dict__))
ABC.C=DotFunctions('C',(),dict(ABC.C.__dict__))
