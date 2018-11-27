
class Counter(type):
    def __new__(metaclasse,classname,superclasses,diction):
        diction['counter']=0
        return super().__new__(metaclasse,classname,superclasses,diction)

    def __call__(Class, *args):
        Class.counter+=1
        return type.__call__(Class,*args)
