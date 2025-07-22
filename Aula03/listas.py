# 1. Criação de uma lista
alunos = ["Maria", "João", "Ana"]
print(alunos)

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
print(alunos)