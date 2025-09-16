#Pergunte o salário do funcionário e calcule o valor do aumento. > 1250 é 10% e <= é 15%

salario = int(input("Qual é o seu salário? "))

if salario <= 1250:
    novo_salario = float(salario*1.15)
    print(f"Seu aumento será de 15% e novo salário será {novo_salario:.2f}")
else:
    novo_salario = float(salario*1.1)
    print(f"Seu aumento será de 10% e novo salário será {novo_salario:.2f}")