import logging, time

# Configuração do logger
logger = logging.getLogger(__name__)
def retry(func, max_attempts=3, delay=1):
    for attempt in range(1, max_attempts + 1):
        try:
            return func()
        except Exception as e:
            logger.warning(f"Tentativa {attempt} falhou: {e}")
            if attempt == max_attempts:
                logger.error(f"Todas as {max_attempts} tentativas falharam")
                raise
            time.sleep(delay * attempt)  # Backoff exponencial