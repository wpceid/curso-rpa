### Instalação e Configuração Inicial

# Instalação simples via pip:
# pip install pyautogui

# Dependências adicionais para Linux:
# sudo apt-get install python3-tk python3-dev

### Controle do Mouse: Movimentação

import pyautogui

# Define uma pausa entre comandos
pyautogui.PAUSE = 0.5

# Obtém o tamanho da tela
largura, altura = pyautogui.size()
print(f"Resolução: {largura}x{altura}")

# Move para o centro da tela
pyautogui.moveTo(largura/2, altura/2)

# Move 100 pixels para direita
pyautogui.moveRel(100, 0)

### Controle do Mouse: Cliques e Scroll

import pyautogui

# Clique simples na posição atual
# pyautogui.click()

# Clique em coordenadas específicas
# pyautogui.click(x=100, y=200)

# Clique direito
# pyautogui.rightClick(x=100, y=200)

# Clique duplo
# pyautogui.doubleClick(x=100, y=200)

# Rolar para baixo (valor positivo)
# pyautogui.scroll(-300)

# Rolar para cima (valor negativo)
# pyautogui.scroll(300)

# Arrastar e soltar (drag and drop)
# pyautogui.dragTo(300, 400, duration=1)

### Controle do Teclado: Digitação

import pyautogui
import pyperclip

# Digita texto na posição atual do cursor
# pyautogui.write('Olá, mundo!')

# Digita com intervalo entre caracteres
# pyautogui.write('Digitando devagar', interval=0.25)

# Para textos com acentuação, uma alternativa é:
# Copia o texto para a área de transferência
# texto = "Olá! Este texto tem acentuação."
# pyperclip.copy(texto)
# Cola o texto com Ctrl+V
# pyautogui.hotkey('ctrl', 'v')

### Controle do Teclado: Teclas Especiais

import pyautogui

# Pressiona Enter
# pyautogui.press('enter')

# Pressiona várias teclas em sequência
# pyautogui.press(['tab', 'tab', 'space'])

# Combinações de Teclas
# Pressiona Alt+Tab
# pyautogui.hotkey('alt', 'tab')
# Ctrl+C para copiar
# pyautogui.hotkey('ctrl', 'c')
# Ctrl+Alt+Del
# pyautogui.hotkey('ctrl', 'alt', 'del')

### Captura de Tela: Screenshots

import pyautogui

# Captura toda a tela
# screenshot = pyautogui.screenshot()
# Salva a captura em um arquivo
# screenshot.save('minha_captura.png')

# Captura uma região específica
# (x, y, largura, altura)
# regiao = pyautogui.screenshot(region=(0, 0, 300, 400))

### Captura de Tela: Análise de Pixel

import pyautogui

# Obtém a cor RGB do pixel na posição (100, 200)
# cor = pyautogui.pixel(100, 200)
# print(f"Cor RGB: {cor}")

# Verifica se um pixel tem determinada cor
# if pyautogui.pixelMatchesColor(100, 200, (255, 0, 0)):
#     print("O pixel é vermelho!")

### Localização de Imagens na Tela

import pyautogui
# import cv2 # Necessário para o parâmetro confidence

# Localizando Elementos Visuais
# posicao = pyautogui.locateOnScreen('botao.png')
# if posicao:
#     print(f"Encontrado em: {posicao}")
#     # Clica no centro da imagem encontrada
#     pyautogui.click(pyautogui.center(posicao))
# else:
#     print("Imagem não encontrada!")

# Busca com 70% de confiança
# posicao = pyautogui.locateOnScreen(
#     'icone.png',
#     confidence=0.7,
#     grayscale=True
# )

### Mecanismos de Segurança

import pyautogui

# Ativa o mecanismo de segurança
pyautogui.FAILSAFE = True
# Adiciona pausa de 0.5s entre comandos
pyautogui.PAUSE = 0.5

### Projeto Prático: Automação do Bloco de Notas

import pyautogui
import time

# Passo 1: Abrir o Bloco de Notas
# Pressiona a tecla Windows
pyautogui.press('win')
time.sleep(1)
# Digita "notepad" e pressiona Enter
pyautogui.write('notepad')
pyautogui.press('enter')
time.sleep(2)  # Aguarda abrir

# Passo 2: Digitar Conteúdo
# Texto a ser digitado
mensagem = """Olá! Este é um texto
digitado automaticamente
pelo PyAutoGUI.
Estou aprendendo automação!"""
# Digita o texto
pyautogui.write(mensagem)
time.sleep(1)

# Passo 3: Salvar o Arquivo
# Pressiona Ctrl+S para salvar
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
# Digita o nome do arquivo
pyautogui.write('meu_arquivo_automatico.txt')
pyautogui.press('enter')

### Dicas e Boas Práticas: Adicione Pausas

import time
import pyautogui

# Após clicar em um botão
# pyautogui.click(x, y)
# time.sleep(2)  # Espera 2 segundos

### Dicas e Boas Práticas: Trate Erros

import pyautogui

# Exemplo de tratamento de erro (requer 'botao.png' para funcionar)
# try:
#     pos = pyautogui.locateOnScreen('botao.png')
#     pyautogui.click(pyautogui.center(pos))
# except:
#     print("Botão não encontrado!")