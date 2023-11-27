import pandas as pd
import smtplib
from email.mime.text import MIMEText
import ssl
from email.message import EmailMessage

def send_email(subject, message, to, from_email, email_password):
    # Configurações do servidor de e-mail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465

    # Criar a mensagem
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to
    msg.set_content(message, subtype='html')

    # Enviar o e-mail
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(from_email, email_password)
        server.send_message(msg)

filial = 'BoaViagem'

def reposicao(filial, from_email, email_password, to_email):
    df = pd.read_csv(f'estoque-{filial}.csv')

    # Lista para armazenar as mensagens de alerta
    alertas = []
    # Lista para armazenar os produtos que precisam de reposição
    produtos_reposicao = []

    enviar_email = False
    for index, row in df.iterrows():
        if row['Quantidade'] < 0.1 * row['Quantidade Inicial']:
            enviar_email = True
            alerta = f'<br><br>Filial: {filial}<br>Alerta: A quantidade do produto <b>{row["Item"]}</b> está <b>abaixo de 10%</b> da quantidade inicial.<br>'
            alertas.append(alerta)

            # Adicionar o produto à lista de reposição
            produtos_reposicao.append([row["Item"], row["Quantidade"], row["Quantidade Inicial"]])

    if enviar_email:
        print('\nATENÇÃO! Alerta de reposição do estoque.')
        # Enviar Email
        # Juntar as mensagens de alerta em uma única string
        message = '\n'.join(alertas)

        # Adicionar a mensagem ao corpo do e-mail
        body = f"""
        <div style="color:black;">
            <h1>Olá, gerente</h1>
            <h2>Segue abaixo a lista de produtos que precisam de reposição de estoque:</h2>
            <h3>{message}</h3>
        </div>
        """
        # Enviar o e-mail
        send_email('Alerta de reposição de estoque', body, to_email, from_email, email_password)

        # Enviar alerta Fornecedores
        user_input = input('Deseja restocar os produtos? (S/N) ')
        if user_input.upper() == 'S':
            print("\n-- Produtos que precisam de reposição --\n")
            for produto in produtos_reposicao:
                print(f'Produto: {produto[0]}')
                print(f'Quantidade: {produto[1]}')
                print(f'Quantidade Inicial: {produto[2]}')
                print('------------------------')
            escolha_produto = input('Digite o nome do produto que deseja restocar: ')
            if escolha_produto in [item[0] for item in produtos_reposicao]:
                produto = [item for item in produtos_reposicao if item[0] == escolha_produto][0]
                df = pd.read_csv(f'estoque-{filial}.csv')

                # Atualizar o estoque
                quantidade_reposicao = int(input(f"Digite a quantidade que você deseja repor ao produto '{produto[0]}': "))
                df.loc[df['Item'] == produto[0], 'Quantidade'] = produto[1] + (quantidade_reposicao)
                df.loc[df['Item'] == produto[0], 'Quantidade Inicial'] = produto[1] + (quantidade_reposicao)
                # Nome do Fornecedor
                fornecedor = input(f"Digite o nome do fornecedor: ")
                df.loc[df['Item'] == produto[0], 'Fornecedor'] = fornecedor
                # Salvar o arquivo csv
                df.to_csv('estoque.csv', index=False)
                print('\nEstoque atualizado com sucesso!')
            else:
                print('\nProduto não encontrado. Tente novamente.\n')
                reposicao(filial, from_email, email_password, to_email)
        else:
            print('\nFinalizando...')              
    else:
        print('\nNão há alertas de reposição do estoque.')    
reposicao(filial, 'notify.saboresdomundo@gmail.com', 'krqn nkyy zeql xkbk', 'maria.hiarita@souunit.com.br')