# Função sem Retorno
def saudacao(nome):
    """Exibe uma mensagem de saudação."""
    print(f"Olá, {nome}! Bem-vindo(a)!")
    # Chamando a função
saudacao("Mundo")
# Saída: Olá, Mundo!

def adicionar_item(lista, item):
    """Adiciona item à lista e mostra mensagem."""
    lista.append(item)
    print(f"{item} foi adicionado!")


# Função com Retorno
def calcular_media(notas):
    """Calcula a média de uma lista de notas."""
    if not notas:
        return 0
    return sum(notas) / len(notas)
# Chamando a função com retorno
media_calculada = calcular_media([7.5, 8.0, 9.5])
print(f"Média: {media_calculada}") # Média: 8.33

def obter_info():
    """Retorna múltiplos valores como tupla."""
    return "Ana", 25, "Engenharia"


# Função com Posicionais
def exibir_dados(nome, idade, curso):
    print(f"{nome}, {idade} anos, {curso}")
# Chamada
exibir_dados(22, "Sistemas", "Carlos")


# Função com Nomeados
# Mesma função, ordem diferente
exibir_dados(
    nome="Carlos",
    idade=22,
    curso="Sistemas"
)

# Função com Parâmetros Padrão
def cadastrar(nome, idade, curso="Python"):
    print(f"{nome}, {idade}, {curso}")
cadastrar("Maria", 19)  # Curso = Python
cadastrar("João", 25, "Java")  # Curso = Java

# Função com Argumentos Variáveis
def media(*notas):
    """Calcula a média de uma sequência de notas."""
    if not notas:
        return 0
    return sum(notas) / len(notas)
print(f"Média de (7, 8, 9, 10): {media(7, 8, 9, 10)}")
print(f"Média de (5, 6): {media(5, 6)}")

def perfil(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
    return dados

x = perfil(nome="Ana", idade=22, curso="Engenharia")
print(x)

# Importando módulo completo
import math
resultado = math.sqrt(16) # 4.0

# Importando função específica
from math import sqrt
resultado = sqrt(16) # 4.0
print(resultado)

# Importando com alias
import math as m
resultado = m.sqrt(16) # 4.0

# Importando módulo próprio
# Em arquivo utils.py
# def validar_cpf(cpf): # lógica de validação
#     return True
# Em arquivo principal
from utils import validar_cpf

validacao = validar_cpf("123.456.789-09")
print(validacao)