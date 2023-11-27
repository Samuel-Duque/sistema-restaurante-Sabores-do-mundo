import pandas as pd
from classes import *
from funcoes_registro import Cadastro_Funcionarios, lista_cadastrados, cargos



# nome_gerente = input('Digite seu nome: ')
# password_gerente = input('Digite sua senha: ')
# novo_usuario = pessoa(nome_gerente, password_gerente, cargo='Gerente')



#case 2 vai servir para acessar a uma aba em que podera ser visto os funcionarios registrados, escala de horas, registro de horas e
#avalição de desempenho dos funcionarios
def Menu_gerente_filial(filial):
    print('''  
        1 - Cadastrar novo funcionário
        2 - Gestão de equipe
        3 - Sair
    ''')
    opcao_menu_gerente = int(input('Digite a opção desejada: '))
    match opcao_menu_gerente:
        case 1:
            Cadastro_Funcionarios(lista_cadastrados, cargos, filial)
            Menu_gerente_filial()
        case 2:
            
            Menu_gerente_filial()
        case 3:
            print('Saindo...')
        case _:
            print('Opção inválida!')
            Menu_gerente_filial()    
                
Menu_gerente_filial()