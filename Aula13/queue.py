import queue
import threading
import time

# Criação da fila de tarefas
tarefa_queue = queue.Queue()

# Função para processar tarefas
def processar_tarefa():
    while True:
        try:
            # Obtém tarefa da fila (aguarda até 5 segundos)
            tarefa = tarefa_queue.get(timeout=5)
            print(f"Processando: {tarefa}")
            time.sleep(2) # Simula processamento
            tarefa_queue.task_done()
        except queue.Empty:
            print("Fila vazia, encerrando thread")
            break

# Criação de threads de processamento
for i in range(3):
    t = threading.Thread(target=processar_tarefa)
    t.daemon = True
    t.start()

# Adicionando tarefas à fila
for i in range(10):
    tarefa_queue.put(f"Tarefa {i}")

# Aguarda conclusão de todas as tarefas
tarefa_queue.join()