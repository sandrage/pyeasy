from person import Person
import datetime
class Wizard(Person):
    def __init__(self, name, lastname, birthday):
        super().__init__(name,lastname,birthday)

    def get_age(self):
        return (datetime.date.today() - self.get_birthday()).days//365

    def set_age(self, newvalue):
        self.set_birthday(datetime.date(datetime.date.today() - newvalue).days/365, self.get_birthday.month, self.get_birthday.day)

    def __repr__(self):
        return "{0}, {1}".format(super().__repr__(), self.age)

    age = property(get_age, set_age, None, "Age del wizard")

if __name__=='__main__':
    print(Wizard("Sandra", "Gergawi", datetime.date(1995,5,4)))
