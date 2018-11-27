from person import Person
class Worker(Person):
    def __init__(self,name,lastname,birthday,pay_per_hour):
        super(Worker,self).__init__(name,lastname,birthday)
        self._pay_per_hour = pay_per_hour
    def set_pay_per_hour(self, newval):
        self._pay_per_hour=newval
    def get_pay_per_hour(self):
        return self._pay_per_hour
    def get_day_salary(self):
        return 8*self.get_pay_per_hour()
    def get_week_salary(self):
        return 5*self.day_salary
    def get_month_salary(self):
        return 4*self.week_salary
    def get_year_salary(self):
        return 12*self.month_salary
    day_salary = property(get_day_salary,None,None,"Day salary")
    week_salary= property(get_week_salary, None, None, "Week salary")
    month_salary = property(get_month_salary, None,None,"Month salary")
    year_salary = property(get_year_salary,None,None,"Year salary")
