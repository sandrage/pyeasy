

def memoization(func):
    def args_wrapper(*args):
        if not(args_wrapper.cache.get(args)):
            args_wrapper.cache[args]=func(*args)
        else:
            print("### cached value for {0} --> {1}".format(args,args_wrapper.cache[args]))
        return args_wrapper.cache[args]
    args_wrapper.cache={}
    return args_wrapper

@memoization
def fact(n):
    return (n>0 and n * fact(n-1)) or 1

@memoization
def fibo(n):
    return n>1 and fibo(n-1)+fibo(n-2) or 1

@memoization
def sum(x,y):
    return (y!=0 and sum(x+1,y-1)) or x
