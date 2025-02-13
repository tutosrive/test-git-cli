from model.Company import Company
from model.Employee import Employee
import chromolog as ch

# Colour printer
printer = ch.Print()

# Companies
my_company = Company('SRM-TRG', 'Empresa Unipersonal', 'Microempresa', 'Terciario', 'Privada')

# Employees
srm = Employee('Santiago Marin', 19, 60, 180, 'Developer', 2500000, 'SRM')
trg = Employee('Tutos Rive', 19, 60, 180, 'Developer', 2500000, 'SRM-TRG')

# Imprimir información
printer.suc(my_company.add_employees(srm, trg))
printer.inf(my_company.get_all_employees_str())
printer.suc(my_company)