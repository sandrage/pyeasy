from worker import Worker
class Spell(type):
    def __new__(metaclasse, classname, superclasses, diction):
        print("{0}, {1}, {2}, {3}".format(metaclasse, classname, superclasses, diction))
        for (attr,value) in Worker.__dict__.items():
            if not(diction.get(attr)):
                print("{0} not in dict".format(attr))
                diction[attr]=value
        return type.__new__(metaclasse,classname,superclasses,diction)
