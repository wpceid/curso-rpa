## Aula 2 – Lógica e Fluxo de Controle

Nesta aula, você vai aprender como o Python “pensa”: estruturas como `if`, `for` e `while` permitirão que você tome decisões e repita tarefas no código — uma base essencial para qualquer automação.

---

## 📘 Conteúdo da Aula

### 1. Variáveis e Tipos
```python
nome = "João"
idade = 20
altura = 1.75
ativo = True
print(type(nome), type(idade), type(altura), type(ativo))
```

### 2. Operadores
```python
print(5 + 2)  # Soma
print(5 > 2)  # Relacional
print(True and False)  # Lógico
```

### 3. Estruturas de Decisão
```python
idade = int(input("Digite sua idade: "))
if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")
```

### 4. Laços de Repetição
```python
for i in range(5):
    print("Contador:", i)

contador = 0
while contador < 5:
    print("Enquanto:", contador)
    contador += 1
```

### 5. break e continue
```python
for numero in range(1, 10):
    if numero == 5:
        break
    print("Com break:", numero)

for numero in range(1, 10):
    if numero % 2 == 0:
        continue
    print("Com continue:", numero)
```

---

## 🧠 Exercício 1: Classificador de idade

```python
idade = int(input("Informe a idade: "))
if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")
```

## 🔢 Exercício 2: Soma de pares de 1 a 100

```python
soma = 0
for numero in range(1, 101):
    if numero % 2 == 0:
        soma += numero
print("Soma dos pares de 1 a 100:", soma)
```

---

## ✅ Boas práticas de nomeação

| Boa Prática              | Exemplo bom            | Exemplo ruim     |
|--------------------------|------------------------|------------------|
| Use nomes descritivos    | `idade`, `soma_pares`  | `x`, `var1`      |
| Use snake_case no Python | `total_vendas`         | `TotalVendas`    |
| Evite abreviações vagas  | `quantidade_clientes`  | `qtd_cli`        |

---
