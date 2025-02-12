from Person import Person
from Company import Company

class Employee(Person):
    def __init__(self, name:str, age:float | int, weight:float | int, height:int, job:str, salary:float, company:Company):
        super().__init__(name, age, weight, height)

company_trg = Company('SRM-TRG', 'Empresa Unipersonal', 'Microempresa', 'Sector terciario', 'Privada')
srm = Employee('Santiago', 19, 60, 180, 'Developer', 2500000, company_trg)
print(srm)