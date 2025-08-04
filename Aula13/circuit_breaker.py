import time

class CircuitBreaker:
    def __init__(self, max_falhas=5, reset_timeout=60):
        self.falhas = 0
        self.max_falhas = max_falhas
        self.reset_timeout = reset_timeout
        self.estado = "FECHADO"  # FECHADO, ABERTO, MEIO-ABERTO
        self.ultima_falha = 0

    def executar(self, func):
        if self.estado == "ABERTO":
            if time.time() - self.ultima_falha > self.reset_timeout:
                self.estado = "MEIO-ABERTO"
            else:
                raise Exception("Circuit breaker aberto")

        try:
            resultado = func()
            if self.estado == "MEIO-ABERTO":
                self.estado = "FECHADO"
                self.falhas = 0
            return resultado
        except Exception as e:
            self.falhas += 1
            self.ultima_falha = time.time()
            if self.falhas >= self.max_falhas:
                self.estado = "ABERTO"
            raise