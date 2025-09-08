

# Funções para gerenciar usuários
def cadastrar_usuario(usuarios, nome, idade, email):
    if email in usuarios:
        return False
    usuarios[email] = {
        "nome": nome,
        "idade": idade,
        "email": email
    }
    return True

def buscar_usuario(usuarios, nome):
    for email, dados in usuarios.items():
        if dados["nome"].lower() == nome.lower():
            return dados
    return None

def remover_usuario(usuarios, nome):
    for email, dados in usuarios.items():
        if dados["nome"].lower() == nome.lower():
            del usuarios[email]
            return True
    return False