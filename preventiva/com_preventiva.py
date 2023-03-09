
class FamilyExpenses:
    #Prevenindo entradas inadequadas pelo usuario
    def __init__(self):
        self.expenses = dict()

    def add_expense(self, name, amount):
        if amount <= 0:
            raise ValueError(f"Informe um valor maior que 0 para {name}")
        self.expenses[name] = amount

    def remove_expense(self, name):
        if name in self.expenses:
            del self.expenses[name]
        else:
            raise ValueError(f'Despesa {name} não encontrada.')

    def total_expenses(self):
        total = 0
        for expense in self.expenses.values():
            total += expense
        return total

    def list_expenses(self):
        for name, amount in self.expenses.items():
            print(f'{name}: R$ {amount}')
            
        print(f'Total de despesas: R$ {self.total_expenses()}')


def try_exception_add(fam, name, value):
    try:
        fam.add_expense(name, value)
    except ValueError as e:
        print(e.args[0])    
        
def try_exception_remove(fam, name):
    try:
        fam.remove_expense(name)
    except ValueError as e:
        print(e.args[0]) 
# exemplo de uso
fam = FamilyExpenses()
try_exception_add(fam, 'comida', 200)
try_exception_add(fam, 'transporte', 150)
try_exception_add(fam, 'aluguel', 0) 
fam.list_expenses()
try_exception_remove(fam, 'comida')
fam.list_expenses()