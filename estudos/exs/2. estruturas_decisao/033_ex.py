#Leia 3 números e mostre qual é o maior e qual é o menor

a, b, c = map(int, input("Digite 3 números: ").split())

num = [a,b,c]

maior = max(num)
menor = min(num)

print(f"O maior número é o {maior} e o menor número é o {menor}.")