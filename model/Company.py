class Company:
    def __init__(self, name:str, legal_form:str, size_type:str, economic_sector:str, property_type:str, employees:list = None) -> None:
        self.name:str = name
        self.legal_form:str = legal_form
        self.size_type:str = size_type
        self.economic_sector:str =economic_sector
        self.property_type:str = property_type
        self.employees:list = []
    
    def __str__(self):
        return f'Nombre Empresa: {self.name}\nForma Jurídica: {self.legal_form}\nTamaño: {self.size_type}\nSector Económico: {self.economic_sector}\nPropiedad: {self.property_type}\n'

    def add_employees(self, *employyes) -> dict:
        for employee in employyes:
            if employee.__class__.__name__ != 'Employee':
                return {'error': 'Los empleados deben ser de tipo "Employee"'}
            self.employees.append(employee)
        return {'ok': True}

    def get_all_employees_str(self) -> str:
        employees_str:str = ''
        for employee in self.employees:
            employees_str += f'----\n{employee.__str__()}\n'
        employees_str += '----\n'
        return employees_str