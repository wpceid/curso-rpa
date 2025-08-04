import requests

# Requisição GET simples
response = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
print(response.status_code)
print(response.json()) # Se a resposta for JSON

# Parâmetros na URL
params = {'start_date': '20180901', 'end_date': '20180930'}
base_url = 'https://economia.awesomeapi.com.br/json/daily/USD-BRL/1?'
response = requests.get(base_url, params=params)
print(response.status_code)
print(response.json()) # Se a resposta for JSON

# Headers na requisição, como token de autenticação ou chave de API
headers = {'Authorization': 'Bearer seu_token_jwt', 'Content-Type': 'application/json'}
response = requests.post('https://economia.awesomeapi.com.br/json/last/USD-BRL', headers=headers, json={'dado': 'valor'})
print(response.status_code)
print(response.json()) # Se a resposta for JSON

# Autenticação via header, como X-API-Key
headers = {'X-API-Key': 'sua_chave_api'}
resposta = requests.get('https://economia.awesomeapi.com.br/json/last/:moedas', headers=headers)

# Autenticação básica (usuário e senha)
resposta = requests.get('https://economia.awesomeapi.com.br/json/last/:moedas', auth=('usuario', 'senha'))