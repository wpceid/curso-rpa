import win32com.client as win32

outlook = win32.Dispatch('outlook.application')
email = outlook.CreateItem(0)

email.To = 'destinatario@email.com'
email.Subject = 'E-mail Automático de Teste'
email.HTMLBody = '<p>Este é um <b>email HTML</b> enviado via Outlook.</p>'

email.Send()