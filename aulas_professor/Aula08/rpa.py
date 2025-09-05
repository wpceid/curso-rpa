from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
# Configurar o driver
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
try:
    navegador.get("https://www.uol.com.br")

    time.sleep(5)

    email_link = navegador.find_element(By.CSS_SELECTOR, 'a[href="https://email.uol.com.br/"]')
    email_link.click()
    time.sleep(5)

    email_input = navegador.find_element(By.ID, 'user')
    email_input.send_keys("teste@uol.com.br")
    time.sleep(5)

    continue_button = navegador.find_element(By.ID, 'button-submit')
    continue_button.click()
    time.sleep(5)

    
finally:
    navegador.quit()