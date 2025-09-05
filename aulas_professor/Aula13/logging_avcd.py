import logging
import logging.handlers
import os
from datetime import datetime

# Configuração do diretório de logs
log_dir = os.path.join(os.getcwd(), 'logs')
os.makedirs(log_dir, exist_ok=True)

# Nome do arquivo baseado na data
log_file = os.path.join(log_dir, f'rpa_{datetime.now().strftime("%Y%m%d")}.log')

# Configuração do logger principal
logger = logging.getLogger('RPABot')
logger.setLevel(logging.DEBUG)

# Formato detalhado para os logs
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(threadName)s - %(message)s')

# Handler para arquivo com rotação (10 MB por arquivo, máximo 5 arquivos)
file_handler = logging.handlers.RotatingFileHandler(
    log_file, maxBytes=10*1024*1024, backupCount=5)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Handler para console (apenas WARNING e acima)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_handler.setFormatter(formatter)

# Adiciona os handlers ao logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Exemplo de uso
logger.debug("Iniciando configuração do bot")
logger.info("Bot configurado com sucesso")
logger.warning("Timeout detectado, tentando novamente")
logger.error("Falha ao conectar com o servidor")
logger.critical("Processo interrompido por erro crítico")