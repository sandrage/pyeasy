def guarded(condition):
    def functionwrapper(func):
        def wrapper(*args):
            if condition(*args[1:]):
                return func(*args)
        return wrapper
    return functionwrapper
