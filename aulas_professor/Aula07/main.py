import pyautogui
import pandas as pd
import time

largura, altura = pyautogui.size()

pyautogui.press('win')
time.sleep(1)
pyautogui.write('explorador de arquivos')
time.sleep(1)
pyautogui.moveTo(largura/2, altura/2)
pyautogui.moveRel(0, 10)
pyautogui.doubleClick()
time.sleep(20)
pyautogui.write('Projetos\\UNIFAAT\\RPA\\RPA_Aulas\\Aula04\\dados.csv')
time.sleep(3)
pyautogui.press('enter')
