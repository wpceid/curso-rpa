def exibir_menu():
    print("\n===== SISTEMA DE CADASTRO =====")
    print("1. Cadastrar usuário")
    print("2. Listar usuários")
    print("3. Buscar usuário")
    print("4. Remover usuário")
    print("5. Sair")
    return input("Escolha uma opção: ")

def processar_opcao(opcao, usuarios):
    if opcao == "1":
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        email = input("Email: ")
        if cadastrar_usuario(usuarios, nome, idade, email):
            print("Usuário cadastrado com sucesso!")
        else:
            print("Email já cadastrado!")
    # Outras opções implementadas...