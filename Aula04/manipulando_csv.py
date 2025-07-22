import csv
# Leitura de CSV
# Assumes 'dados.csv' is in the same directory as this script.
with open('dados.csv', 'r', encoding='utf-8') as arquivo:
    leitor_csv = csv.reader(arquivo)
    for linha in leitor_csv:
        print(linha)
# Escrita de CSV
# Creates 'saida.csv' in the same directory as this script.
with open('saida.csv', 'w', newline='', encoding='utf-8') as arquivo:
    escritor_csv = csv.writer(arquivo)
    escritor_csv.writerow(['Nome', 'Idade'])
    escritor_csv.writerow(['Ana', 30])

    