# Criando um conjunto
linguagens = {"Python", "Java", "C++"}
# Adicionando elemento
linguagens.add("JavaScript")
print(linguagens)
# Tentando adicionar duplicata
linguagens.add("Python") # Ignorado
print(linguagens)
# Verificando pertinência
print("Python" in linguagens) # True