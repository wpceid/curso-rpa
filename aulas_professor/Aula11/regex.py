import re

texto = """Contatos:
João Silva - joao.silva@empresa.com.br - (11) 98765-4321
Maria Santos - maria@tech.org - (21) 91234-5678
Pedro Alves - pedro.a@consultoria.net - (31) 99876-5432 - 111.111.111-11 - https://www.exemplo.com/gustavo/ -  01/01/2020"""


# Encontrar o primeiro email
padrao_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
primeiro_email = re.search(padrao_email, texto)
if primeiro_email:
    print("Primeiro email encontrado:", primeiro_email.group())

# Encontrar todos os emails
todos_emails = re.findall(padrao_email, texto)
print("Todos os emails:", todos_emails)

# Encontrar todos os telefones
padrao_telefone = r'\(\d{2}\)\s\d{5}-\d{4}'
telefones = re.findall(padrao_telefone, texto)
print("Telefones encontrados:", telefones)

# Substituir formato de telefone
novo_texto = re.sub(padrao_telefone, 'TEL: \\g<0>', texto)
print(novo_texto)


# Exemplos Praticos:
# Padrão: 000.000.000-00
padrao_cpf = r'\d{3}\.\d{3}\.\d{3}-\d{2}'
cpfs = re.findall(padrao_cpf, texto) # Assume 'texto' de um contexto anterior com CPFs

padrao_url = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/[a-zA-Z0-9./_-]*)?'
urls = re.findall(padrao_url, texto) # Assume 'texto' de um contexto anterior com URLs

# Formatos: DD/MM/AAAA ou DD-MM-AAAA
padrao_data = r'\d{2}[/-]\d{2}[/-]\d{4}'
datas = re.findall(padrao_data, texto) # Assume 'texto' de um contexto anterior com datas

print("CPFs encontrados:", cpfs)
print("URLs encontradas:", urls)
print("Datas encontradas:", datas)

#