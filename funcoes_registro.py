
from classes import *
import csv
import pandas as pd


cargos = ['Gerente','Chef de cozinha','Cliente']
def Cadastro_Gerente(lista_cadastrados,cargos): 
    nome_cadastro = input("Digite o seu nome para cadastro: ")
    senha_cadastro = input("Digite sua senha para cadastro: ")
    senha_cadastro_verificacao = input("Digite sua senha novamente para cadastro: ")
    
    if senha_cadastro != senha_cadastro_verificacao:
        print("Senhas diferentes!")
        Cadastro_Gerente(lista_cadastrados,cargos)
    cadastro_novo = pessoa(nome_cadastro, senha_cadastro,cargos[0])
    lista_cadastrados.append(cadastro_novo)

def Login(lista_cadastrados, cargos):
    entrada_nome = input("Digite o seu nome cadastrado: ")
    entrada_senha = input("Digite sua senha: ")
    for pessoa in lista_cadastrados:
        if pessoa.nome == entrada_nome and pessoa.password == entrada_senha:
            print("\nLOGADO COM SUCESSO")
            print(f"Nome: {pessoa.nome}\nCargo:{pessoa.cargo}")
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



lista_cadastrados = []
def main():
    
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
                main()
            case '2':
                Login(lista_cadastrados,cargos)
                main()
            case '3':
                break


def gestao_equipe():
    for pessoas in lista_cadastrados:
        print(f"Nome: {pessoas.nome}")

