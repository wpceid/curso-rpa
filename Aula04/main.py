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