#Escolha um número entre 0 e 5 e peça para o usuário adivinhar e informe se ele acertou ou errou

num_certo = 2

num_escolhido = int(input("Escolha um número entre 0 e 5: "))

if num_certo == num_escolhido:
 print("Você acertou!")
else: print("Você errou!")