import inspect
def decorator(f):
    def wrapper(*args):
        sig = inspect.signature(f)
        for i in range(1,len(args[0:])):
            args[0].__dict__[list(sig.parameters.items())[i][0]] = args[i]
        return f(*args)
    return wrapper

class AutoInit(type):
    def __new__(Class, classname, subs, dictions):
        dictions['__init__'] = decorator(dictions['__init__'])
        return type.__new__(Class, classname, subs, dictions)
