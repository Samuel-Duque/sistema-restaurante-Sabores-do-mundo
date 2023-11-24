import pandas as pd

class Cliente:
    def __init__(self, nome, password, cargo='Cliente'):
        self.nome = nome
        self.password = password
        self.cargo = cargo

    def falar(self):
        print(f'Eu sou {self.nome} e sou um {self.cargo}')

    def permissoes(self):
        if self.cargo == 'Gerente':
            return 'Permissão para acesso a todos os relatórios'
        elif self.cargo == 'Chef de Cozinha':
            return 'Permissão para acesso a relatórios de cozinha'
        elif self.cargo == 'Cliente':
            return 'Sem permissões especiais'

        
class Chef_de_Cozinha(Cliente):
    def __init__(self, nome, password):
        super().__init__(nome, password, cargo='Chef de Cozinha')

    def permissoes(self):
        return 'Permissão para acesso a relatórios de cozinha e pedidos'


class Restaurante():
    def __init__(self, nome):
        self.nome = nome
        self.estoque_df = pd.read_csv(f'estoque-Duque_de_caxias.csv')
p1 = Chef_de_Cozinha('João', '123')
if p1.cargo == 'Chef de Cozinha':
    print('Permissão para acesso a todos os relatórios')