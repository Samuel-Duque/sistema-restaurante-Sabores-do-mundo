from cardapio import *

class pessoa:
    def __init__(self, nome, password, cargo='Cliente'):
        self.nome = nome
        self.password = password
        self.cargo = cargo
        self.historico = []

    def registrar_historico(self, historico):
        self.historico = historico

    def permissoes(self):
        if self.cargo == 'Gerente':
            return 'Permissão para acesso a todos os relatórios'
        elif self.cargo == 'Chef de Cozinha':
            return 'Permissão para acesso a relatórios de cozinha'
        elif self.cargo == 'Cliente':
            return 'Sem permissões especiais'
        
        
class Chef_de_Cozinha(pessoa):
    def __init__(self, nome, password):
        super().__init__(nome, password, cargo='Chef de Cozinha')

    def permissoes(self):
        return 'Permissão para acesso a relatórios de cozinha e pedidos'

    def preparar_comida(self):
        comida = input("Qual comida você quer preparar?: ")
        for item in estoque:
            if item in cardapio[comida] and estoque[item] >= cardapio[comida][item]:
                estoque[item] -= cardapio[comida][item]
            elif item in cardapio[comida] and estoque[item] >= cardapio[comida][item]:
                print(f'Você não tem ingredientes suficientes para preparar {comida}.')
                break

        print(f'{comida} preparada com sucesso!')
        
class Gerente_filial(pessoa):
    def __init__(self, nome, password):
        super().__init__(nome, password, cargo='Gerente_filial')

    def permissoes(self):
        return 'Permissão para acesso a todos os relatórios e pedidos'
    
p1 = pessoa('João', '1234')
p1 = Chef_de_Cozinha(p1.nome, p1.password)
print(p1.preparar_comida())