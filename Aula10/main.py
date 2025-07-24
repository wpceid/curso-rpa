import requests
from bs4 import BeautifulSoup

def extrair_noticias(url): 
    # Configurando o cabeçalho para simular um navegador 
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' }  
    # Fazendo a requisição HTTP 
    resposta = requests.get(url, headers=headers)  
    # Verificando se a requisição foi bem-sucedida 
    if resposta.status_code != 200: 
        return f"Erro ao acessar o site. Código: {resposta.status_code}"  
    # Parseando o HTML 
    soup = BeautifulSoup(resposta.text, 'html.parser')  
    # Encontrando os títulos das notícias (ajuste o seletor conforme o site) 
    titulos = soup.select('.feed-post-link')  
    # Extraindo e retornando os resultados 
    return [titulo.text for titulo in titulos]

# Chamando a função com uma URL de exemplo
noticias = extrair_noticias('https://g1.globo.com/')
for i, noticia in enumerate(noticias, 1): 
    print(f"{i}. {noticia}")
