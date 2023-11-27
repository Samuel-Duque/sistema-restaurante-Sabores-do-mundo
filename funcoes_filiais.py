from classes import *
from funcoes_registro import *

def main_gerente(lista_cadastrados,cargos):
    while True:
        print('\n')
        print("-*"*30)
        print(' '*23,"TELA DE LOGIN")
        print("-*"*30)
        print("1. Login filial")
        print("2. Registrar filial")
        print("3. Sair")
        entrada = input("Digite a opcao desejada: ")
        match entrada:
            case '1':
                nome_escolha_filial = input("Digite o nome da filial: ")
                nome_arquivo = f"funcionarios-{nome_escolha_filial}.csv"
                try:
                    with open(nome_arquivo, 'r', newline='') as arquivo:
                        print("Filial encontrada!")
                        Menu_gerente_filial(cria_filial_nome(nome_escolha_filial))
                except FileNotFoundError:
                    print("Filial não encontrada!")
                    main_gerente(lista_cadastrados,cargos)
            case '2':
                nome_criacao_filial = input("Digite o nome da filial:")
                cria_filial_nome(nome_criacao_filial)
                main_gerente(lista_cadastrados,cargos)
            case '3':
                break
def Cadastro_Funcionarios(lista_cadastrados, cargos, filial):
    nome_cadastro = input("Digite nome para cadastro: ")
    idade_cadastro = input("Digite a idade para cadastro: ")
    senha_cadastro = input("Digite senha para cadastro: ")
    senha_cadastro_verificacao = input("Digite sua senha novamente para cadastro: ")
    historico_funcionario_cadastro = input("Digite o historico de trabalho: ")
    
    if senha_cadastro != senha_cadastro_verificacao:
        print("Senhas diferentes!")
        # Cadastro_Gerente(lista_cadastrados,cargos)

    for index,cargo in enumerate(cargos):
        print(f"{index} - {cargo}")
    
    escolher_cargo= int(input("Digite o index do cargo desejado: "))
    listas_nomes = []
    lista_idade = []
    lista_cargo = []
    lista_historico = []
    
    listas_nomes.append(nome_cadastro)
    lista_idade.append(idade_cadastro)
    lista_cargo.append(cargos[escolher_cargo])
    lista_historico.append(historico_funcionario_cadastro)

    cadastro_novo = pessoa(nome_cadastro, senha_cadastro, historico_funcionario_cadastro, idade_cadastro, cargos[escolher_cargo])
    if cargos[escolher_cargo] == 'Chef de cozinha':
        cadastro_novo = Chef_de_Cozinha(cadastro_novo.nome, cadastro_novo.password, cadastro_novo.historico, cadastro_novo.idade,)
    with open(filial,'r', newline='') as arquivo:
        if arquivo.read(1) == '':
            
            df = pd.DataFrame({
                "Nome": listas_nomes,
                "Idade": lista_idade,
                "Cargo": lista_cargo,
                "Historico": lista_historico
            })
            df.to_csv(filial, sep=";", index=False, mode = 'a')
            
        else:
            
            df = pd.DataFrame({
                "Nome": listas_nomes,
                "Idade": lista_idade,
                "Cargo": lista_cargo,
                "Historico": lista_historico
            })
            df.to_csv(filial, sep=";", index=False, mode = 'a', header=False)

    lista_cadastrados.append(cadastro_novo)

def cria_filial_nome(local):
    nome_arquivo = f"funcionarios-{local}.csv"
    with open(nome_arquivo,'a', newline='') as arquivo:
        print()
        return nome_arquivo
    
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
            Menu_gerente_filial(filial)
        case 2:
            
            gestao_equipe(filial)
        case 3:
            print('Saindo...')
        case _:
            print('Opção inválida!')
            Menu_gerente_filial(filial)    
        

def gestao_equipe(filial):
    with open(filial, "r", newline = '')as arquivo2:
        arquivo = pd.read_csv(arquivo2, sep=";")
        for nome in arquivo["Nome"]:
            print(f"Nome: {nome}")
    escolha_nome = input("Digite o nome do funcionario: ")
    escala_data = input("Digite a data da escala: ")
    escala_horas = input("Digite a escala de horas: ")
    avaliacao_desempenho = input("Digite o desempenho : ")

    nome_funcionario = []
    data_funcionario = []
    horas_funcionario = []
    desempenho_funcionario = []

    nome_funcionario.append(escolha_nome)
    data_funcionario.append(escala_data)
    horas_funcionario.append(escala_horas)
    desempenho_funcionario.append(avaliacao_desempenho)

    dados = pd.DataFrame({
        "Nome": nome_funcionario,
        "Escala": data_funcionario,
        "Horario": horas_funcionario,
        "Avaliação de desempenho": desempenho_funcionario
    })
    dados.to_csv(f"gestao de {filial}", sep=";", index=False, mode = 'a')
main_gerente(lista_cadastrados,cargos)