
def Log(beforeOrAfter):
    def wrapper_func(func):
        def wrapper(*args):
            if beforeOrAfter=='before':
                print("*** I'm going to call {0}()".format(func.__name__))
                return func(*args)
            else:
                result = func(*args)
                print("*** I've called {0}()".format(func.__name__))
                return result
        return wrapper
    return wrapper_func

def PreCondition(func):
    def wrapper(*args):
        print("*** {0}() has been called with :- {1}".format(func.__name__,args[1:]))
        return func(*args)
    return wrapper

def PostCondition(func):
    def wrapper(*args):
        result = func(*args)
        print("*** the value the call should return is {0}() :- {1}".format(func.__name__,result))
        return result
    return wrapper

beforeLog = Log('before')
afterLog = Log('after')
beforePreCondition = PreCondition
afterPreCondition = PreCondition
beforePostCondition = PostCondition
afterPostCondition = PostCondition

def weaving(classn,elems):
    class MetaWeave(type):
        def __new__(metacl,classname,subs,diction):
            for elem in elems:
                if elem[0] in diction:
                    diction[elem[0]]=elem[1](diction[elem[0]])
                    diction[elem[0]].__name__=elem[0]
            return type.__new__(metacl,classname,subs,diction)
    return MetaWeave(classn.__name__,(),dict(classn.__dict__))
