class Cliente():
    def __init__(self, nome, password):
        self.nome = nome
        self.password = password

def Cadastro(lista_cadastrados):
    nome_cadastro = input("Digite o seu nome para cadastro: ")
    senha_cadastro = input("Digite sua senha para cadastro: ")
    senha_cadastro_verificacao = input("Digite sua senha novamente para cadastro: ")
    if senha_cadastro != senha_cadastro_verificacao:
        print("Senhas diferentes!")
        Cadastro(lista_cadastrados)
    cadastro_novo = Cliente(nome_cadastro, senha_cadastro)
    lista_cadastrados.append(cadastro_novo)

def Login(lista_cadastrados):
    entrada_nome = input("Digite o seu nome cadastrado: ")
    entrada_senha = input("Digite sua senha: ")
    for pessoa in lista_cadastrados:
        if pessoa.nome == entrada_nome and pessoa.password == entrada_senha:
            print("LOGADO COM SUCESSO")
        elif pessoa.nome == entrada_nome and pessoa.password != entrada_senha:
            print("SENHA INCORRETA")

def main():
    lista_cadastrados = []
    while True:
        print('\n')
        print("-*"*30)
        print(' '*23,"TELA DE LOGIN")
        print("-*"*30)
        print("1. Cadastrar funcionario")
        print("2. LOGIN")

        entrada = input("Digite a opcao desejada: ")
        match entrada:
            case '1':
                Cadastro(lista_cadastrados)
            case '2':
                Login(lista_cadastrados)
if __name__ == '__main__':
    main()
