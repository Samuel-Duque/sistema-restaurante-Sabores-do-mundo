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

filial = 'Mae'

def reposicao(filial, from_email, email_password, to_email):
    print(filial)
    if filial == 'Mae':
        # Ler o arquivo csv
        df = pd.read_csv('estoque.csv')
    elif filial == 'Boa Viagem':
        # Ler o arquivo csv
        df = pd.read_csv('estoque-BoaViagem.csv')
    elif filial == 'Setubal':
        # Ler o arquivo csv
        df = pd.read_csv('estoque-Setubal.csv')

    # Lista para armazenar as mensagens de alerta
    alertas = []
    enviar_email = False
    for index, row in df.iterrows():
        if row['Quantidade'] < 0.1 * row['Quantidade Inicial']:
            print('Há alertas de reposição de estoque.')
            enviar_email = True
            alerta = f'<br><br>Filial: {filial}<br>Alerta: A quantidade do produto <b>{row["Item"]}</b> está <b>abaixo de 10%</b> da quantidade inicial.<br>'
            alertas.append(alerta)

    if enviar_email:
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
    else:
        print('Não há alertas de reposição de estoque.')    
reposicao(filial, 'vinciuscarmo71@gmail.com', 'danc ykwr odan rfew', 'vinciuscarmo95@gmail.com')