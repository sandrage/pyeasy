import datetime
import functools
from person import Person
class Student(Person):
    def __init__(self,name,lastname,birthday,lectures):
        super(Student,self).__init__(name,lastname,birthday)
        self._lectures = lectures
    def get_grade_average(self):
        return functools.reduce(sum,map(lambda x: x[1],self._lectures.items()))/len(self._lectures)
    def get_lectures(self):
        return self._lectures
    def set_lectures(self, newval):
        self._lectures = newval
    def __repr__(self):
        return super(Student,self).__repr__()+" Lectures: {0}".format(self._lectures)
    grade_average = property(get_grade_average,None,None,"Grade average")


if __name__ == '__main__':
    s1=Student("Sandra","Gergawi",datetime.date(2017,6,11),{"matematica":27})
    print(s1.grade_average)
