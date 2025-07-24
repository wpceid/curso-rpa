### Baixar o WebDriver

## Baixe o driver correspondente ao seu navegador:
# ChromeDriver para Google Chrome
# GeckoDriver para Firefox
# EdgeDriver para Microsoft Edge

# pip install selenium
# pip install webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
# Configurar o driver
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
try: # Acessar o Google
    navegador.get("https://www.google.com")
    # Encontrar o campo de busca
    campo_busca = navegador.find_element(By.NAME, "q")
    # Digitar um termo de busca
    campo_busca.send_keys("Selenium Python tutorial")
    # Pressionar Enter
    campo_busca.send_keys(Keys.RETURN)
    # Esperar para ver os resultados
    time.sleep(5)
    # Capturar o título dos resultados
    print(f"Título da página: {navegador.title}")
finally: # Fechar o navegador
    navegador.quit()