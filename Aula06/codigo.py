# pip install pyautogui
import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 0.5
largura, altura = pyautogui.size()
print(f"Resolução: {largura}x{altura}")
pyautogui.moveTo(largura/2, altura/2)
pyautogui.moveRel(100, 0)
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

pyautogui.press('win')
time.sleep(1)

pyautogui.write('notepad')
pyautogui.press('enter')
time.sleep(2)

mensagem = """Olá! Este é um texto
digitado automaticamente
pelo PyAutoGUI.
Estou aprendendo automação!"""

pyautogui.write(mensagem)
time.sleep(1)

pyautogui.hotkey('ctrl', 's')
time.sleep(1)

pyautogui.write('meu_arquivo_automatico.txt')
pyautogui.press('enter')