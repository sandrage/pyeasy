import inspect

def mysetattr(self,obj,value):
    caller = inspect.currentframe().f_back
    caller_name = caller.f_code.co_name
    caller_type = caller.f_locals.get('self').__class__.__name__
    obj_class = self.__class__.__name__
    print("caller: {0}, caller_type: {1}, obj_type: {2}".format(caller_name,caller_type,obj_class))
    if not(caller_type==obj_class and caller_name =='__init__'):
        if not(self.__dict__.get(obj)):
            raise AssertionError("Stai cercando di settare l'attributo {0} nel metodo {1} della classe {2}, dovresti farlo in {3}".format(obj,caller_name,caller_type,obj_class))
    object.__setattr__(self,obj,value)

class EnforceOO(type):
    def __new__(metacl,classname,subs,dct):
        dct['__setattr__']=mysetattr
        return type.__new__(metacl,classname,subs,dct)
