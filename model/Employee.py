from model.Person import Person

class Employee(Person):
    def __init__(self, name:str, age:float | int, weight:float | int, height:int, job:str, salary:float, company:str):
        super().__init__(name, age, weight, height)
        self.salary = salary
        self.company = company
    
    def __str__(self):
        return f'{super().__str__()}Salario: {self.salary}\nEmpresa: {self.company}'