#Escolha um número entre 0 e 5 e peça para o usuário adivinhar e informe se ele acertou ou errou

from random import randint

num_certo = randint(0, 5)

num_escolhido = int(input("Escolha um número entre 0 e 5: "))

if num_certo == num_escolhido:
 print(f"Você acertou! Eu pensei no número {num_certo}")
else: print(f"Você errou! Eu pensei no número {num_certo}")