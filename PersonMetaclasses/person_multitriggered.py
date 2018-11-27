import datetime
from multitriggered import MultiTriggeredMethod
class Person(metaclass=MultiTriggeredMethod):
    def __init__(self,name,lastname,birthday):
        self._name=name
        self._lastname=lastname
        self._birthday=birthday

    def set_name(self, newval):
        self._name=newval
    def set_lastname(self,newval):
        self._lastname=newval
    def set_birthday(self,newval):
        self._birthday=newval

    def get_name(self):
        return self._name
    def get_lastname(self):
        return self._lastname
    def get_birthday(self):
        return self._birthday

    def __repr__(self):
        return "Nome {0}, Cognome {1}, Data di nascita {2}".format(self._name,self._lastname,self._birthday)

if __name__=='__main__':
    p1 = Person("Sandra","Gergawi",datetime.date(2010,5,11))
    p2 = Person("Sandra", "Gergawi", datetime.date(2010,5,11))

    print("chiamata uno di p1 {0}".format(p1.get_name()))
