class Employee:
    inc_percent = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def sal(self):
        self.pay = int(self.pay * self.inc_percent)

    def fullname(self):
        return self.first + ' ' + self.last

    def __repr__(self):
        return f"Employee('{self.first}','{self.last}','{self.pay}')"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"


emp_1 = Employee('Aarthi', 'Sivasankar', 34323)
emp_2 = Employee('Jaya', 'SP', 67767)
print(repr(emp_1))
print(str(emp_1))
print("Now printing just the obj**")
print(emp_1)
print("-----------------")
print(repr(emp_2))
print(str(emp_2))
print("Now printing just the obj** emp2")
print(emp_2)
print("------ Modify from X ----------")
print("------ More changes ----------")
print("This statement is printed from DEVELOP BRANCH")
