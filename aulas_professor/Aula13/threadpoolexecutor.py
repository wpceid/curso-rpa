from concurrent.futures import ThreadPoolExecutor

def processar_item(item):
    # Lógica de processamento
    return f"Resultado: {item}"

itens = list(range(100))

with ThreadPoolExecutor(max_workers=5) as executor:
    resultados = list(executor.map(
        processar_item,
        itens
    ))