import inspect


def decorateinit(self,*args):
    i=0
    self.superclass={}
    for supercls in self.superclasses:
        signature = inspect.signature(supercls.__init__)
        self.superclass[supercls]=supercls(*args[i:i+len(signature.parameters)-1])
        i+=len(signature.parameters)-1
def decorate_getattr(obj,attr):
    for superclass,superclass_instance in obj.superclass.items():
        if hasattr(superclass_instance,attr):
            return getattr(superclass_instance,attr)
def Twins(supercls):
    class TwinsObj(type):
        def __new__(metac,cls,subs,dct):
            dct['superclasses']=supercls
            dct['__init__']=decorateinit
            dct['__getattr__']=decorate_getattr
            return type.__new__(metac,cls,subs,dct)
    return TwinsObj
