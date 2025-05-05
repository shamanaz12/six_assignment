class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

e = Employee("Ali", 50000, "123-45-6789")
print(e.name)        # Public
print(e._salary)     # Protected
# print(e.__ssn)     # Will raise error
print(e._Employee__ssn)  # Name mangling
