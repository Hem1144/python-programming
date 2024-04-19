class Instructor:
    def __init__(self, name, addeess):
        self.name = name
        self.address = addeess
        self.followers = 0


instructor_1 = Instructor("Hemlal", "Melamchi")
print(instructor_1.name)
print(instructor_1.followers)
# instructor_1.name = "Hemlal"
# instructor_1.address = "Melamchi"
# print(instructor_1.address)
instructor_2 = Instructor("Dulal", "Sindhupalchok")
print(instructor_2.address)
# instructor_2.name = "Dulal"
# print(instructor_2.name)


class Employee:
    def set_salary(self, value):
        self.salary = value
        return self.salary


e = Employee()
payroll = e.set_salary(50000)
print(str(payroll))
print(e.salary)
