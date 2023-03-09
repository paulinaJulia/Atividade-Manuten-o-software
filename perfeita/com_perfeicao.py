from abc import ABC, abstractmethod


class Builder(ABC):
    #Utilizando o padrão de projeto Builder
    @abstractmethod
    def add_or_update(self, name, amount) -> 'Builder':
        pass
    
    @abstractmethod
    def remove(self, name) -> 'Builder':
        pass
    
    @abstractmethod
    def build(self) -> dict:
        pass

class FamilyExpenses(Builder):
    def __init__(self):
        self.expenses = dict()

    def add_or_update(self, name, amount) -> Builder:
        if amount <= 0:
            raise ValueError(f"Informe um valor maior que 0 para {name}")
        self.expenses.update({
            f'{name}': amount,
        })
        
        return self

    def remove(self, name) -> Builder:
        if self.expenses.get(name):
            self.expenses.pop(name)
        else:
            raise ValueError(f'Despesa {name} não encontrada.')
        return self
    
    def build(self) -> dict:
        return self.expenses


def try_exception_inserts(fam: Builder):
    try:
        fam.add_or_update('comida', 150) \
            .add_or_update('transporte', 200) \
            .add_or_update('aluguel', 1200)
    except ValueError as e:
        print(e.args[0])    
        
def try_exception_removes(fam: Builder):
    try:
        fam.remove('comida')\
            .remove('teste')
    except ValueError as e:
        print(e.args[0])
        
def prepare_list(fam: Builder): 
    total = 0 
    for name, amount in fam.build().items():
        total += amount
        print(f'{name}: R$ {amount}')
        
    print(f'Total de despesas: R$ {total}')
# exemplo de uso
fam = FamilyExpenses()
try_exception_inserts(fam)  
try_exception_removes(fam)
prepare_list(fam)