# Abrir um arquivo
with open('arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
# Escrever em um arquivo
with open('saida.txt', 'w') as arquivo:
    arquivo.write('Olá, mundo!')
# Adicionar conteúdo
with open('log.txt', 'a') as arquivo:
    arquivo.write('Nova linha\n')