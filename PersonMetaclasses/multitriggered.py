import types
def decorator(f):
    def wrapper(*args):
        if not(args[0].__dict__.get(f)):
            print("l'attributo non esisteva: ")
            args[0].__dict__[f]=0
        if args[0].__dict__[f] <2:
            print("Il counter è minore di 2")
            args[0].__dict__[f]+=1
            result=None
        elif args[0].__dict__[f]==2:
            args[0].__dict__[f]=0
            result = f(*args)
        return result
    return wrapper

class MultiTriggeredMethod(type):
    def __new__(Metaclasse,classname,superclasses,diction):
        for (attr,value) in diction.items():
            if isinstance(value,types.FunctionType) and not attr=='__init__' and not attr=='__repr__':
                print("Trovato metodo: {0} {1}".format(attr,value))
                diction[attr]=decorator(value)
        return type.__new__(Metaclasse,classname,superclasses,diction)
