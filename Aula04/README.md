### Manipulação de Arquivos: Operações Básicas

# Abrir um arquivo
with open('arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
# Escrever em um arquivo
with open('saida.txt', 'w') as arquivo:
    arquivo.write('Olá, mundo!')
# Adicionar conteúdo
with open('log.txt', 'a') as arquivo:
    arquivo.write('Nova linha\n')

### Manipulação de Arquivos: Trabalhando com Arquivos CSV

import csv
# Leitura de CSV
with open('dados.csv', 'r', encoding='utf-8') as arquivo:
    leitor_csv = csv.reader(arquivo)
    for linha in leitor_csv:
        print(linha)
# Escrita de CSV
with open('saida.csv', 'w', newline='', encoding='utf-8') as arquivo:
    escritor_csv = csv.writer(arquivo)
    escritor_csv.writerow(['Nome', 'Idade'])
    escritor_csv.writerow(['Ana', 30])

### Tratamento de Exceções: Estrutura try, except, else, finally

def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    except TypeError:
        print("Erro: Certifique-se de que os inputs são números.")
    else:
        print(f"Resultado: {resultado}")
    finally:
        print("Operação de divisão concluída.")

### Tratamento de Exceções: Usando raise

def sacar(saldo, valor):
    if valor > saldo:
        raise ValueError("Saldo insuficiente!")
    return saldo - valor

### Sistema de Logs: Configuração Básica

import logging
# Configuração básica
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Esta é uma mensagem informativa.")
logging.warning("Esta é uma mensagem de aviso.")
logging.error("Esta é uma mensagem de erro.")
logging.debug("Esta é uma mensagem de depuração.")

### Sistema de Logs: Logs em Arquivo

import logging
# Configuração para log em arquivo
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

### Sistema de Logs: Configuração Avançada

import logging
# Criar um logger personalizado
logger = logging.getLogger('meu_app')
logger.setLevel(logging.DEBUG)

# Criar um handler para arquivo
file_handler = logging.FileHandler('app_avancado.log')
file_handler.setLevel(logging.INFO)

# Criar um handler para console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Definir formato para os handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Adicionar handlers ao logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.debug("Mensagem de depuração.")
logger.info("Mensagem informativa.")

### Prática & Colaboração: Projeto Integrado - main.py

import logging
import csv

# Configuração de logs
logging.basicConfig(filename='processamento.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def processar_arquivo_dados(nome_arquivo_entrada, nome_arquivo_saida):
    try:
        with open(nome_arquivo_entrada, 'r', encoding='utf-8') as infile:
            leitor = csv.reader(infile)
            cabecalho = next(leitor) # Pula o cabeçalho

            with open(nome_arquivo_saida, 'w', newline='', encoding='utf-8') as outfile:
                escritor = csv.writer(outfile)
                escritor.writerow(cabecalho + ['Status']) # Adiciona coluna de status

                for linha_num, linha in enumerate(leitor, 2): # Começa a contar do 2 para a linha do arquivo
                    try:
                        # Exemplo de validação: garantir que a idade é um número
                        idade = int(linha[1]) # Supondo que a idade está na segunda coluna
                        if idade < 0:
                            raise ValueError("Idade negativa")
                        
                        # Processamento bem-sucedido
                        escritor.writerow(linha + ['Processado'])
                        logging.info(f"Linha {linha_num}: Processada com sucesso. Dados: {linha}")

                    except ValueError as ve:
                        escritor.writerow(linha + [f'Erro: {ve}'])
                        logging.warning(f"Linha {linha_num}: Erro de validação - {ve}. Dados: {linha}")
                    except IndexError:
                        escritor.writerow(linha + ['Erro: Formato de linha inválido'])
                        logging.error(f"Linha {linha_num}: Erro de formato - linha incompleta. Dados: {linha}")
                    except Exception as e:
                        escritor.writerow(linha + [f'Erro inesperado: {e}'])
                        logging.critical(f"Linha {linha_num}: Erro inesperado - {e}. Dados: {linha}")

    except FileNotFoundError:
        logging.error(f"Erro: Arquivo '{nome_arquivo_entrada}' não encontrado.")
        print(f"Erro: Arquivo '{nome_arquivo_entrada}' não encontrado.")
    except Exception as e:
        logging.critical(f"Erro fatal ao abrir ou processar o arquivo: {e}")
        print(f"Erro fatal: {e}")

if __name__ == "__main__":
    print("Iniciando o processamento de dados...")
    # Crie um arquivo 'dados.csv' de exemplo para testar:
    # Nome,Idade,Cidade
    # Alice,25,São Paulo
    # Bob,30,Rio de Janeiro
    # Carol,-5,Belo Horizonte
    # David,40
    # Eve,abc,Porto Alegre
    processar_arquivo_dados('dados.csv', 'saida_processada.csv')
    print("Processamento concluído. Verifique 'processamento.log' e 'saida_processada.csv'.")