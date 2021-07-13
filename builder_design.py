class Student:

    def set_age(self, age_):
        self.age = age_

    def get_age(self):
        return self.age

    def set_name(self, name_):
        self.name = name_

    def get_name(self):
        return self.name

    def set_address(self, address_):
        self.address = address_

    def get_address(self):
        return self.address


class StudentBuilder:
    def __init__(self):
        self.student = Student()

    def age(self, age_):
        self.student.set_age(age_)
        return self

    def name(self, name_):
        self.student.set_name(name_)
        return self

    def address(self, address_):
        self.student.set_address(address_)
        return self

    def build(self):
        return self.student


abc = StudentBuilder().name("ABC").age(29).address("abbbb").build()
de = StudentBuilder().name("de").build()

ram = StudentBuilder().age(23).build()
print(abc)
print(de)
print(ram)