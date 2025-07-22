### Estruturas de Dados: Listas

# 1. Criação de uma lista
alunos = ["Maria", "João", "Ana"]
# 2. Adição de um elemento ao final da lista
alunos.append("Carlos")
# A lista agora é: ["Maria", "João", "Ana", "Carlos"]
# 3. Acesso a um elemento pelo seu índice
# Acessa o primeiro elemento (índice 0)
print(alunos[0])  # Saída: Maria
# 4. Modificação de um elemento
# Altera o valor no índice 1 de "João" para "Pedro"
alunos[1] = "Pedro"
# Ao final de todas as operações, a lista 'alunos' será:
# ["Maria", "Pedro", "Ana", "Carlos"]

### Estruturas de Dados: Tuplas

# Criando uma tupla
coordenadas = (10.5, 20.8)
# Acessando elemento
print(coordenadas[1])  # 20.8
# Tentando modificar (erro)
# coordenadas[0] = 15.0  # TypeError
# Tupla com um item
nota = (9.5,)  # Vírgula é necessária

### Estruturas de Dados: Dicionários

# Criando um dicionário
aluno = {
    "nome": "Ana Silva",
    "idade": 20,
    "curso": "Ciência da Computação"
}
# Acessando valores
print(aluno["nome"])  # Ana Silva
# Adicionando novo par
aluno["semestre"] = 3

### Estruturas de Dados: Conjuntos (Sets)

# Criando um conjunto
linguagens = {"Python", "Java", "C++"}
# Adicionando elemento
linguagens.add("JavaScript")
# Tentando adicionar duplicata
linguagens.add("Python") # Ignorado
# Verificando pertinência
print("Python" in linguagens) # True

### Funções em Python: Funções Sem Retorno

def saudacao(nome):
    """Exibe uma mensagem de saudação."""
    print(f"Olá, {nome}! Bem-vindo(a)!")
    # Chamando a função
saudacao("Maria")
# Saída: Olá, Maria!

def adicionar_item(lista, item):
    """Adiciona item à lista e mostra mensagem."""
    lista.append(item)
    print(f"{item} foi adicionado!")

### Funções em Python: Funções Com Retorno

def calcular_media(notas):
    """Calcula a média de uma lista de notas."""
    if not notas:
        return 0
    return sum(notas) / len(notas)
# Chamando a função com retorno
media = calcular_media([7.5, 8.0, 9.5])
print(f"Média: {media}") # Média: 8.33

def obter_info():
    """Retorna múltiplos valores como tupla."""
    return "Ana", 25, "Engenharia"

### Parâmetros de Funções: Posicionais

def exibir_dados(nome, idade, curso):
    print(f"{nome}, {idade} anos, {curso}")
# Chamada
exibir_dados("Carlos", 22, "Sistemas")

### Parâmetros de Funções: Nomeados

# Mesma função, ordem diferente
exibir_dados(
    curso="Sistemas",
    nome="Carlos",
    idade=22)

### Parâmetros de Funções: Valores Padrão

def cadastrar(nome, idade, curso="Python"):
    print(f"{nome}, {idade}, {curso}")
cadastrar("Maria", 19)  # Curso = Python
cadastrar("João", 25, "Java")  # Curso = Java

### Parâmetros de Funções: Arbitrários

def media(*notas):
    return sum(notas) / len(notas)
media(7, 8, 9, 10) # 4 notas
media(5, 6) # 2 notas

def perfil(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

### Modularização com Import: Formas de Importação

# Importando módulo completo
import math
resultado = math.sqrt(16) # 4.0

# Importando função específica
from math import sqrt
resultado = sqrt(16) # 4.0

# Importando com alias
import math as m
resultado = m.sqrt(16) # 4.0

# Importando módulo próprio
# Em arquivo utils.py
def validar_cpf(cpf): # lógica de validação
    return True
# Em arquivo principal
from utils import validar_cpf