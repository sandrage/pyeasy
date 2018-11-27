import functools,math
directions = {"n":lambda newval:(0,newval), "w":lambda newval:(-1*newval,0), "e":lambda newval:(newval,0), "s":lambda newval:(0,-1*newval)}
def far(map):
    x,y=functools.reduce(lambda a,b: (a[0]+b[0],a[1]+b[1]),[directions[map[c]](int(map[c+1])) for c in range(0,len(map),2)])
    return math.sqrt(x**2+y**2)
