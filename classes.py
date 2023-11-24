# In[ ]:
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
        atualizar_estoque()
        print(f'{comida} preparada com sucesso!')

    def cadastrar_prato(self):
        comida=input("Qual comida você quer cadastrar?: ")
        quantidade = int(input("Digite a quantidade de ingredientes: "))
        ingredientes = {}
        for i in range(quantidade):
            item = input("Qual ingrediente você quer adicionar?: ")
            if item == ingredientes[item]:
                print(f'Você já adicionou {item}.')
                break
            quantidade = int(input(f"Quantos {item} são necessários?: "))
            ingredientes[item] = quantidade
        cardapio[comida] = ingredientes
        print(f'{comida} cadastrada com sucesso!')
        atualizar_cardapio()

class Gerente_filial(pessoa):
    def __init__(self, nome, password):
        super().__init__(nome, password, cargo='Gerente_filial')

    def permissoes(self):
        return 'Permissão para acesso a todos os relatórios e pedidos'
    
p1 = pessoa('João', '1234')
p1 = Chef_de_Cozinha(p1.nome, p1.password)



# %%
