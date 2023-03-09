
class FamilyExpenses:
    #Codigo igual ao Com correção
    def __init__(self):
        self.expenses = dict()

    def add_expense(self, name, amount):
        self.expenses[name] = amount

    def remove_expense(self, name):
        del self.expenses[name]

    def total_expenses(self):
        total = 0
        for expense in self.expenses.values():
            total += expense
        return total

    def list_expenses(self):
        for name, amount in self.expenses.items():
            print(f'{name}: R$ {amount}')
            
        print(f'Total de despesas: R$ {self.total_expenses()}')

# exemplo de uso
fam = FamilyExpenses()
fam.add_expense('comida', 200)
fam.add_expense('transporte', 150)
fam.add_expense('aluguel', 1000)
fam.list_expenses()
fam.remove_expense('comida')
fam.list_expenses()