#Leia um valor em metros e converta em centímetros e milimetros

m = float(input("Insira o valor em metros: "))

cm = m/100
mm = m*1000

print(f"O valor em centímetros é {cm:.2f} e em milímetros é {mm:.2f}")