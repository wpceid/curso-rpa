#Faça um programa que leia algo pelo teclado e mostre seu tipo primitivo e todas as infos possíveis

texto = input("Digite algo: ")
print(f"O tipo é: {type(texto)}")
print(f"É numérico? {texto.isnumeric()}")
print(f"É decimal? {texto.isdecimal()}")
print(f"É texto? {texto.isalpha()}")
print(f"É minúsculo? {texto.islower()}")