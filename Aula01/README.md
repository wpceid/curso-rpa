
## Aula 1 – Ambiente e Primeiros Scripts

Bem-vindo(a) à primeira aula do curso RPA!  
Nesta etapa, vamos configurar seu ambiente de desenvolvimento Python, criar seu primeiro script e publicar tudo em um repositório no GitHub.

---

## 🎯 Objetivos da Aula

- Instalar Python, VS Code e Git
- Criar ambiente virtual com dependências
- Criar conta no GitHub e clonar o repositório
- Escrever e executar um script Python simples
- Publicar o script no repositório remoto

---

## 🛠️ Ferramentas Necessárias

- [Python](https://www.python.org/downloads/) (3.11 ou superior)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Git](https://git-scm.com/downloads)
- Conta no [GitHub](https://github.com)

---

## 🚀 Passo a Passo

### 1. Criar a pasta do projeto

```bash
mkdir aula1_ia
cd aula1_ia
```

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv .venv
```

- **Windows**:
  ```bash
  .venv\Scripts\activate
  ```
- **Linux/macOS**:
  ```bash
  source .venv/bin/activate
  ```

### 3. Instalar dependências

```bash
pip install ipython
```

Salvar no `requirements.txt`:

```txt
ipython
```

---

## 🐙 GitHub

### 4. Criar repositório remoto

1. Acesse [github.com](https://github.com)
2. Crie um novo repositório: `curso-rpa`
3. Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/curso-rpa.git
cd curso-rpa
```

---

## 🧪 Primeiro Script

Crie o arquivo `primeiro_script.py` com o seguinte conteúdo:

```python
nome = "Maria"
idade = 25

print("Olá, mundo!")
print(f"Meu nome é {nome} e eu tenho {idade} anos.")
```

Execute com:

```bash
python primeiro_script.py
```

---

## 📝 Tarefa da Aula

Crie um arquivo chamado `meus_dados.py` com seus dados pessoais.  
Exemplo:

```python
nome = "Gustavo"
idade = 23
cidade = "São Paulo"
hobby = "Moto e Carro"

print(f"Olá! Meu nome é {nome}, tenho {idade} anos, moro em {cidade} e gosto de {hobby}.")
```

---

## ☁️ Publicar no GitHub

```bash
git add .
git commit -m "Adiciona scripts da Aula 1"
git push
```

---

## ✅ Conclusão

Ao final desta aula, você deve ter:
- Ambiente Python configurado
- Scripts funcionando
- Repositório GitHub atualizado

Parabéns por concluir a primeira etapa do curso! 🎉
