class Company:
    def __init__(self, name:str, legal_form:str, size_type:str, economic_sector:str, property_type:str, employees:list = None) -> None:
        self.name:str = name # Nombre de la empresa
        self.legal_form:str = legal_form # Forma jurídica (persona natural, unipersonal, e.t.c.)
        self.size_type:str = size_type # Clasificación por tamaño (microempresa, ...)
        self.economic_sector:str = economic_sector # Sector económico (prima/secunda/terciario)
        self.property_type:str = property_type # Tipo de propiedad (privada, pública, mixta)
        self.employees:list = [] # Lista de empleados (Contiene objetos de tipo Employee)
    
    def __str__(self):
        return f'Nombre Empresa: {self.name}\nForma Jurídica: {self.legal_form}\nTamaño: {self.size_type}\nSector Económico: {self.economic_sector}\nPropiedad: {self.property_type}\nEmpleados: \n{self.get_all_employees_names()}'

    def add_employees(self, *employyes) -> dict:
        """Añadir empleados a la lista de empleados de la empresa

        Args:
            employees (*args): Empleados que se desean agregar
        
        Returns:
            dict: Diccionario.Si hay un error se retornará dentro de este, sino, se retornará un `ok = True`
        """
        for employee in employyes:
            # Validar que el tipo de objeto sea "Employee"
            if employee.__class__.__name__ != 'Employee':
                return {'error': 'Los empleados deben ser de tipo "Employee"'}
            # Agregar cada empleado a la lista
            self.employees.append(employee)
        return {'ok': True}

    def get_all_employees_names(self) -> str:
        """Obtener la lista completa de nombres de los empleados

        Returns:
            str: Lista de nobres
        """
        names:str = ''
        for i, employee in enumerate(self.employees):
            names += f'----\nEmpleado {i + 1}: {employee.name}\n'
        names += '----\n'
        return names

    def get_all_employees_str(self) -> str:
        """Obtener la lista completa de empleados 

        Returns:
            str: Lista de empleados en una cadena de texto con formato: `key: value`
        """
        employees_str:str = ''
        for employee in self.employees:
            employees_str += f'----\n{employee.__str__()}\n'
        employees_str += '----\n'
        return employees_str