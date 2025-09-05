import logging

# Tratamento de Exceções: Estrutura try, except, else, finally
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

# Tratamento de Exceções: Usando raise
def sacar(saldo, valor):
    if valor > saldo:
        raise ValueError("Saldo insuficiente!")
    return saldo - valor

# Sistema de Logs: Configuração Básica

# Configuração básica
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Esta é uma mensagem informativa.")
logging.warning("Esta é uma mensagem de aviso.")
logging.error("Esta é uma mensagem de erro.")
logging.debug("Esta é uma mensagem de depuração.")

# Sistema de Logs: Logs em Arquivo

# Configuração para log em arquivo
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Sistema de Logs: Configuração Avançada

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