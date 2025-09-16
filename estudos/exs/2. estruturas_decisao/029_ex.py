#Leia a velocidade de um carro, se for maior que 80, mostre que ele será multado. A multa será 7 reais para cada km acima do limite

vel_limite = 80

vel_carro = int(input("Qual a velocidade do carro? "))

if vel_carro > vel_limite:
    multa = float((vel_carro - vel_limite)*7)
    print(f"O carro está acima da velocidade! A multa será de R${multa:.2f}!")
print("O carro está dentro da velocidade permitida!")