import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
msg = MIMEMultipart()
msg['From'] = 'seu@email.com'
msg['To'] = 'destino@email.com'
msg['Subject'] = 'Relatório Diário de Cotações'
corpo = 'Segue em anexo o relatório de cotações do dia.'
msg.attach(MIMEText(corpo, 'plain'))

# Anexando arquivo
nome_arquivo = 'relatorio_cotacoes.xlsx'
caminho = os.path.join(os.getcwd(), nome_arquivo)
anexo = open(caminho, 'rb')
parte = MIMEBase('application', 'octet-stream')
parte.set_payload(anexo.read())
encoders.encode_base64(parte)
parte.add_header('Content-Disposition', f'attachment; filename={nome_arquivo}')
msg.attach(parte)
anexo.close()

# Envio do e-mail com anexo
servidor = smtplib.SMTP('smtp.gmail.com', 587)
servidor.starttls()
servidor.login('seu@email.com', 'senha_app')
texto = msg.as_string()
servidor.sendmail(msg['From'], msg['To'], texto)
servidor.quit()
