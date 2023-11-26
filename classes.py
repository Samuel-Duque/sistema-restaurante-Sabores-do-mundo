# In[ ]:
from cardapio import *
import csv
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
        
     
class Filial():
    def __init__(self,nome,arquivo_csv):
        self.nome = nome
        #dicionário para armazenar a quant disponível de cada item no estoque
        self.estoque = {}
        self.arquivo_csv = arquivo_csv
        
    #arquivo no argumento para eu usar o arquivo da filial que eu quero
    def carregar_estoque(self):
        with open(self.arquivo_csv, newline='', encoding='utf-8') as arquivo:
            ler = csv.DictReader(arquivo)
            #itera cada linha do arquivo csv
            for linha in ler:# cada iteração obtem uma linha do arquivo
                item = linha['item']
                quantidade = int(linha['quantidade'])
                self.estoque[item] = quantidade   
                
    def salvar_estoque(self):
        with open(self.arquivo_csv,'w', newline='', encoding='utf-8') as arquivo:
            coluna = ['item','quantidade']
            escrever = csv.DictWriter(arquivo,fieldnames=coluna)
            escrever.writeheader()
            
            for item, quantidade in self.estoque.items():
                escrever.writerow({'item': item, 'quantidade':quantidade})
    def adicionar_produto(self,produto,quantidade):
        self.carregar_estoque()
        if produto in self.estoque:
            self.estoque[produto] += quantidade
        else:
            self.estoque[produto] = quantidade
        self.salvar_estoque()
            
    def remover_produto(self,produto,quantidade):
        self.carregar_estoque()
        
        if produto in self.estoque and self.estoque[produto] >= quantidade:
            self.estoque[produto] -= quantidade
        else:
            print(f"Quantidade insulficiente de {produto} em {self.nome}.")
            
    def mostrar_produto(self):
        print(f"\nEstoque em {self.nome}")
        for produto, quantidade in self.estoque.items():
            print(f"{produto}: {quantidade}")
        
class Chef_de_Cozinha(pessoa):
    def __init__(self, nome, password,filial):
        super().__init__(nome, password, cargo='Chef de Cozinha')
        self.filial = filial

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
    def __init__(self, nome, password,filial):
        super().__init__(nome, password, cargo='Gerente_filial')
        self.filial = filial 

    def permissoes(self):
        return 'Permissão para acesso a todos os relatórios e pedidos'
    
p1 = pessoa('João', '1234')
p1 = Chef_de_Cozinha(p1.nome, p1.password)



# %%
