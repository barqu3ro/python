income_types = ["Salario", "Préstamo", "Aguinaldo", "Salario Escolar"]

def Add_Income_Type (new_income_type):
    income_types.append(new_income_type)

class Income :
    
    def __init__ (self, type, amount):
