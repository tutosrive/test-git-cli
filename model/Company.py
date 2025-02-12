from Employee import Employee

class Company:
    def __init__(self, name:str, legal_form:str, size_type:str, economic_sector:str, property_type:str, employees:list[Employee] | None):
        self.name = name
        self.legal_form = legal_form
        self.size_type = size_type
        self.economic_sector =economic_sector
        self.property_type = property_type
    
    def __str__(self):
        return f'Nombre Empresa: {self.name}\nForma Jurídica: {self.legal_form}\nTamaño: {self.size_type}\nSector Económico: {self.economic_sector}\nPropiedad: {self.property_type}\n'

company_trg = Company('SRM-TRG', 'Empresa Unipersonal', 'Microempresa', 'Sector terciario', 'Privada')
print(company_trg)