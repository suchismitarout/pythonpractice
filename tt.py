class SingleTon:
    __sharedstate = None
    def __init__(self):
        if SingleTon.__sharedstate is None:
            SingleTon.__sharedstate = self
        else:
            raise Exception('you cant create another')

    def get_instance(self):
        if not SingleTon.__sharedstate:
            return SingleTon()
        return SingleTon.__sharedstate


k = SingleTon()
print(k)
l = k.get_instance()
print(l)
o = k.get_instance()
print(o)

class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_age(self, new_age):
        self.age = new_age

    def get_age(self):
        return self.age

    def set_address(self, new_add):
        self.address = new_add

    def get_address(self):
        return self.address

class EmployeeBuilder():
    def __init__(self):
        self.emp = Employee()

    def get_age(self, new_age):
        self.emp.set_age(new_age)
        return self

    def get_address(self, add):
        self.emp.set_address(add)
        return self

    def get_name(self, name):
        self.emp.set_name(name)
        return self
    def build(self):
        return self.emp

emp1 = EmployeeBuilder().get_age(25).get_address('dkl').get_name('nomi').build()
print(emp1)
emp2 = EmployeeBuilder().get_name('raj').build()
print(emp2)