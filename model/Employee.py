from model.Person import Person

class Employee(Person):
    def __init__(self, name:str, age:float | int, weight:float | int, height:int, job:str, salary:float, company:str):
        # Llamar constructor de clase madre
        super().__init__(name, age, weight, height)
        self.salary = salary # Salario
        self.company = company # Empresa
    
    def __str__(self):
        return f'{super().__str__()}Salario: {self.salary}\nEmpresa: {self.company}'