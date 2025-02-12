from model.Company import Company
from model.Employee import Employee

# Companies
my_company = Company('SRM-TRG', 'Empresa Unipersonal', 'Microempresa', 'Terciario', 'Privada')

# Employees
srm = Employee('Santiago Marin', 19, 60, 180, 'Developer', 2500000, 'SRM')
trg = Employee('Tutos Rive', 19, 60, 180, 'Developer', 2500000, 'SRM-TRG')
print(srm.__class__.__name__)

print(my_company.add_employees(srm, trg))

print(my_company.get_all_employees_str())