# main.py - Programa principal
from usuario import cadastrar_usuario, buscar_usuario, remover_usuario

def main():
    # Banco de dados em memória
    usuarios = {}

    # Loop principal do programa
    while True:
        opcao = exibir_menu()

        if opcao == "5":
            print("Saindo do sistema...")
            break

        processar_opcao(opcao, usuarios)

if __name__ == "__main__":
    main()