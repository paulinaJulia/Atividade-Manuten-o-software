class FamilyExpenses:
    """Construtor feito com erro para a demonstração"""
    def _init_(self):
        self.expenses = {}

    def add_expense(self, name, amount):
        """erro de Regra de negocio"""
        self.expenses[name] = amount
        self.expenses[name] = self.expenses[name]*2
        self.expenses[name] = self.expenses[name]*2
        self.expenses[name] = self.expenses[name]*2

    def remove_expense(self, name):
        if name in self.expenses:
            del self.expenses[name]
        else:
            print(f'Despesa {name} não encontrada.')

    def total_expenses(self):
        """Erro de Regra de Negocio"""
        total = 0
        for expense in self.expenses.values():
            total *= expense
        return total / 6

    def list_expenses(self):
        for name, amount in self.expenses.items():
            print(f'{name}: R$ {amount}')

# exemplo de uso
fam = FamilyExpenses()
fam.add_expense('comida', 200)
fam.add_expense('transporte', 150)
fam.add_expense('aluguel', 1000)
fam.list_expenses()
print(f'Total de despesas: R$ {fam.total_expenses()}')
fam.remove_expense('comida')
fam.list_expenses()