import inspect, re


def deepcopy(l):
    newl = list()
    for elem in l:
        if type(elem) is list:
            newl.append(deepcopy(elem))
        else:
            newl.append(elem)
    return newl

def mydel(*args):
    caller = inspect.currentframe().f_back
    try:
        codeinexecution= inspect.getframeinfo(caller).code_context[0]
        vars = re.findall("([A-Za-z]*[a-zA-Z0-9_]*[ ]*)=([ ]*[A-Za-z]*[a-zA-Z0-9_]*)",codeinexecution)
        caller.f_locals[vars[0][0].strip()] = deepcopy(caller.f_locals[vars[0][1].strip()])
    except AttributeError: return



class Antialiasing(type):
    def __new__(metac,cls,subs,dct):
        dct['__del__']=mydel
        return type.__new__(metac,cls,subs,dct)
    def __init__(cls,clsname,subs,dct):
        return subs.__init__(cls,clsname,subs,dct)

list = Antialiasing('list',(list,),dict(list.__dict__))
