import itertools

def memoization(func):
    def wrapper(*args):
        if not(func.__dict__.get("memoiz")) :
            func.__dict__["memoiz"]={}
        if func.__dict__["memoiz"].get(args):
            print("### cached value for {0} --> {1}".format(args,list(func.__dict__["memoiz"].get(args))))
            return func.__dict__["memoiz"].get(args)
        else:
            result = [i for i in func(*args)]
            func.__dict__["memoiz"][args]=result
        return result
    return wrapper

def gray(n):
    if n==1:
        yield from ['0','1']
    else:
        elems=[i for i in gray(n-1)]
        first = list(map(lambda a: ''.join(a),itertools.product('0',elems)))
        second = list(map(lambda a:''.join(a),itertools.product('1',elems[::-1])))
        yield from first
        yield from second
    raise StopIteration

@memoization
def mgray(n):
    if n==1:
        yield from ['0','1']
    else:
        elems = [i for i in mgray(n-1)]
        first = map(lambda a: ''.join(a), itertools.product('0',elems))
        second = map(lambda a:''.join(a),itertools.product('1',elems))
        yield from first
        yield from second
