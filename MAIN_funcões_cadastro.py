from classes import *
from classes import preparar_comida
import time
import csv 
import cardapio
def Cadastro_Gerente(lista_cadastrados,cargos): 
    nome_cadastro = input("Digite o seu nome para cadastro: ")
    senha_cadastro = input("Digite sua senha para cadastro: ")
    senha_cadastro_verificacao = input("Digite sua senha novamente para cadastro: ")
    
    if senha_cadastro != senha_cadastro_verificacao:
        print("Senhas diferentes!")
        Cadastro_Gerente(lista_cadastrados,cargos)
    cadastro_novo = pessoa(nome_cadastro, senha_cadastro,cargos[0])
    lista_cadastrados.append(cadastro_novo)

def Cadastro_Funcionarios(lista_cadastrados, cargos):

    nome_cadastro = input("Digite o seu nome para cadastro: ")
    senha_cadastro = input("Digite sua senha para cadastro: ")
    senha_cadastro_verificacao = input("Digite sua senha novamente para cadastro: ")
    if senha_cadastro != senha_cadastro_verificacao:
        print("Senhas diferentes!")
        Cadastro_Gerente(lista_cadastrados,cargos)

    for index,cargo in enumerate(cargos):
        print(f"{index} - {cargo}")

    escolher_cargo= int(input("Digite o index do cargo desejado: "))
    cadastro_novo = pessoa(nome_cadastro, senha_cadastro,cargos[escolher_cargo])
    if cargos[escolher_cargo] == 'Chef de cozinha':
        cadastro_novo = Chef_de_Cozinha(nome_cadastro, senha_cadastro)
    lista_cadastrados.append(cadastro_novo)



def criar_filial(local):
    nome_arquivo = f"estoque-{local}.csv"
    filial = Filial(local,nome_arquivo)
    with open(nome_arquivo,'w',newline='', encoding='utf-8') as arquivo:
        colunas = ['item','quantidade']
        escrever = csv.DictWriter(arquivo, fieldnames=colunas)
        escrever.writeheader()
    return filial
    
    
    
def Login(lista_cadastrados, cargos):
    entrada_nome = input("Digite o seu nome cadastrado: ")
    entrada_senha = input("Digite sua senha: ")
    for pessoa in lista_cadastrados:
        if pessoa.nome == entrada_nome and pessoa.password == entrada_senha:
            print("\nLOGADO COM SUCESSO")
            print(f"Nome: {pessoa.nome}, Cargo:{pessoa.cargo}")
            if pessoa.cargo == 'Gerente':
                main_gerente(lista_cadastrados, cargos)
        elif pessoa.nome == entrada_nome and pessoa.password != entrada_senha:
            print("\nSENHA INCORRETA")
        else:
            print("\nUsuario não encontrado!")

def Registro(lista_cadastrados):
    for pessoa in lista_cadastrados:
        print(f"Nome: {pessoa.nome},Cargo:{pessoa.cargo}")
        print(f"Permissão: {pessoa.permissoes()}")

def imprimir_cardapio():
    for comida in cardapio.keys():
        print(comida)
def main_chef_de_cozinha(lista_cadastrados,Chef_de_Cozinha,cargos):
    while True:
        print('\n')
        print("-*"*30)
        print(' '*23,"TELA DE LOGIN CHEF DE COZINHA")
        print("-*"*30)
        print("1. Vizualizar Cardápio ")
        print("2. Preparar Comida")
        entrada = input("Digite a opcao desejada: ")
        match entrada:
            case 1:
                imprimir_cardapio()
            case 2:
                imprimir_cardapio()
                preparar_comida()
            
                    
    
def main_gerente(lista_cadastrados,cargos):
    while True:
        print('\n')
        print("-*"*30)
        print(' '*23,"TELA DE LOGIN GERENTE")
        print("-*"*30)
        print("1. Cadastrar Funcionario")
        print("2. Registro")
        print("3. Relatorio")
        print("4. Monitoramento em tempo real")
        print("5. SAIR")
        entrada = input("Digite a opcao desejada: ")
        match entrada:
            case '1':
                Cadastro_Funcionarios(lista_cadastrados,cargos)
            case '2':
                Registro(lista_cadastrados)
            case '5':
                break

            
def main():
    lista_cadastrados = []
    cargos=['Gerente','Chef de cozinha','Cliente']
    while True:
        print('\n')
        print("-*"*30)
        print(' '*23,"TELA DE LOGIN")
        print("-*"*30)
        print("1. Cadastrar Gerente")
        print("2. LOGIN")
        print("3. SAIR")
        entrada = input("Digite a opcao desejada: ")
        match entrada:
            case '1':
                Cadastro_Gerente(lista_cadastrados,cargos)
            case '2':
                Login(lista_cadastrados,cargos)
                
            case '3':
                break
if __name__ == '__main__':
    main()
