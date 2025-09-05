# pip install pyautogui
# pip install opencv-python
# pip install pillow
import cv2
import pyautogui
import time

print(pyautogui.size())
print(pyautogui.position())

# Configurações de segurança
pyautogui.PAUSE = 0.5 # Pausa entre comandos
pyautogui.FAILSAFE = True # Mecanismo de emergência

def setup():
    # Pressionando a tecla Windows do notebook
    pyautogui.press('win')
    # Abringo o Navegador X
    pyautogui.write('Edge')
    # Pressionando Enter para abrir o navegador
    pyautogui.press('enter')
    time.sleep(2)

    pyautogui.write('https://uol.com.br')
    pyautogui.press('enter')
    time.sleep(3)
    botao = pyautogui.locateOnScreen('uol_logo.png')
    time.sleep(3)
    if botao is None:
        raise Exception("Botão não encontrado na tela")


def preencher_formulario(dados):
    """Preenche o formulário com os dados fornecidos"""
    print("Preenchendo formulário com dados...")


def aguardar_elemento(imagem, max_tentativas=10):
    tentativas = 0
    while tentativas < max_tentativas:
        try:
            pos = pyautogui.locateOnScreen(imagem)
            return pos
        except:
            tentativas += 1
            time.sleep(1)
    raise Exception("Timeout aguardando elemento")

def verificar_sucesso():
    print("Verificando sucesso da operação...")
    return True

def main():
    dados = {
        'nome': 'João Silva',
        'email': 'joao@exemplo.com',
    }
    setup()
    preencher_formulario(dados)
if __name__ == "__main__":
    main()