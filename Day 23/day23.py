class Employee:
    def __init__(self, name='', age=0, salary=0.0):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_salary(self, salary):
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary

# Membuat objek Employee dan mengimplementasikan semua method
employee = Employee()

# Menggunakan method set untuk mengubah atribut
employee.set_name('John Doe')
employee.set_age(30)
employee.set_salary(50000.0)

# Menggunakan method get untuk mendapatkan nilai atribut
print(f'Name: {employee.get_name()}')
print(f'Age: {employee.get_age()}')
print(f'Salary: {employee.get_salary()}')
