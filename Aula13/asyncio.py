import asyncio
import aiohttp
import time

async def buscar_dados(session, url, nome_tarefa):
    print(f"Iniciando {nome_tarefa}")
    inicio = time.time()
    async with session.get(url) as response:
        resultado = await response.text()
    tempo = time.time() - inicio
    print(f"{nome_tarefa} concluída em {tempo:.2f}s")
    return resultado[:100] # Retorna primeiros 100 caracteres

async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3",
        "https://jsonplaceholder.typicode.com/posts/4",
    ]
    async with aiohttp.ClientSession() as session:
        tarefas = [
            buscar_dados(session, url, f"Tarefa {i}")
            for i, url in enumerate(urls)
        ]
        resultados = await asyncio.gather(*tarefas)
    for i, resultado in enumerate(resultados):
        print(f"Resultado {i}: {resultado}")

# Executa o loop de eventos assíncrono
asyncio.run(main())