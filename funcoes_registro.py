from classes import *
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

def Cadastro_Funcionarios(lista_cadastrados, cargos):

    nome_cadastro = input("Digite nome para cadastro: ")
    idade_cadastro = input("Digite a idade para cadastro: ")
    senha_cadastro = input("Digite senha para cadastro: ")
    senha_cadastro_verificacao = input("Digite sua senha novamente para cadastro: ")
    historico_funcionario_cadastro = input("Digite o historico de trabalho: ")
    
    if senha_cadastro != senha_cadastro_verificacao:
        print("Senhas diferentes!")
        Cadastro_Gerente(lista_cadastrados,cargos)

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



    cadastro_novo = pessoa(nome_cadastro, senha_cadastro,cargos[escolher_cargo])
    if cargos[escolher_cargo] == 'Chef de cozinha':
        cadastro_novo = Chef_de_Cozinha(cadastro_novo.nome, cadastro_novo.password)
    df = pd.DataFrame({
        "Nome": listas_nomes,
        "Idade": lista_idade,
        "Cargo": lista_cargo,
        "Historico": lista_historico
    })
    df.to_csv("filia_tal.csv", sep=";", index=False)
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


def main_gerente(lista_cadastrados,cargos):
    while True:
        print('\n')
        print("-*"*30)
        print(' '*23,"TELA DE LOGIN")
        print("-*"*30)
        print("1. Cadastrar Funcionario")
        print("2. Registro")
        print("2. Relatorio")
        print("3. SAIR")
        entrada = input("Digite a opcao desejada: ")
        match entrada:
            case '1':
                Cadastro_Funcionarios(lista_cadastrados,cargos)
            case '2':
                Registro(lista_cadastrados)
            case '3':
                break

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


if __name__ == '__main__':
    Cadastro_Funcionarios(lista_cadastrados,cargos)