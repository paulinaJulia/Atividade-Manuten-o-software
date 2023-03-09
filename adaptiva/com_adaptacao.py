
class FamilyExpenses:
    def __init__(self, balance):
        """Criando instancia de um dicionario, manuseando o saldo"""
        self.expenses = dict()
        self.balance = balance
        self.__init_balance = balance

    def add_expense(self, name, amount):
        """Adicionando"""
        self.expenses[name] = amount

    def remove_expense(self, name):
        """removendo"""
        del self.expenses[name]

    def total_expenses(self):
        """Pegando o total de gastos  e subtraindo do valor inicial """
        total = 0
        self.balance = self.__init_balance #pegando valor que foi inicializado
        for expense in self.expenses.values():
            total += expense
        self.balance -= total
        return total

    def list_expenses(self):
        """Listando o total de despesas e O valor final do saldo"""
        for name, amount in self.expenses.items():
            print(f'{name}: R$ {amount}')
            
        print(f'Total de despesas: R$ {self.total_expenses()}')
        print(f'Saldo Total: R$ {self.balance}')

# exemplo de uso
fam = FamilyExpenses(5000)
fam.add_expense('comida', 200)
fam.add_expense('transporte', 150)
fam.add_expense('aluguel', 1000)
fam.list_expenses()
fam.remove_expense('comida')
print("Valor Após remoção:")
fam.list_expenses()