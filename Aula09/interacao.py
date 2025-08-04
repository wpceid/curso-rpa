import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

print("Iniciando demonstração de Automação Web com Selenium...")

# 1. Configuração do WebDriver
try:
    driver = webdriver.Chrome()
    driver.maximize_window() # Maximiza a janela para melhor visualização
    driver.implicitly_wait(10) # Espera implícita de 10 segundos para todos os elementos
    print("WebDriver Chrome iniciado e configurado com espera implícita de 10s.")
except Exception as e:
    print(f"Erro ao iniciar o WebDriver: {e}")
    print("Certifique-se de ter o ChromeDriver instalado e no PATH do sistema.")
    exit()

# URL de um site de demonstração para interação
# Usaremos um site de teste público para simular as interações.
# Para este exemplo, usaremos o site The Internet by Herokuapp para login simulado
driver.get("https://the-internet.herokuapp.com/login")
print(f"Navegando para: {driver.current_url}")

# --- Demonstração de Localizadores e Interações Básicas ---
print("\n--- Demonstrando Localizadores e Interações Básicas ---")

# Localizador por ID: O mais confiável, deve ser único na página.
try:
    username_field = driver.find_element(By.ID, "username")
    print("Elemento 'username' encontrado por ID.")
    username_field.send_keys("tomsmith") # Digita texto
    print("Digitado 'tomsmith' no campo username.")
except Exception as e:
    print(f"Erro ao localizar/interagir com 'username' por ID: {e}")
    driver.save_screenshot("erro_username_id.png") # Captura screenshot em caso de falha

# Localizador por Name: Útil para formulários, pode não ser único.
try:
    password_field = driver.find_element(By.NAME, "password")
    print("Elemento 'password' encontrado por Name.")
    password_field.send_keys("12345678")
    print("Digitado 'SuperSecretPassword!' no campo password.")
except Exception as e:
    print(f"Erro ao localizar/interagir com 'password' por Name: {e}")
    driver.save_screenshot("erro_password_name.png")

# Localizador por CSS Selector: Sintaxe concisa, geralmente mais rápido.
try:
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    print("Botão de login encontrado por CSS Selector.")
    login_button.click() # Clica no elemento
    print("Clicado no botão de login.")
except Exception as e:
    print(f"Erro ao localizar/interagir com botão de login por CSS Selector: {e}")
    driver.save_screenshot("erro_login_button_css.png")

# --- Demonstração de Espera Explícita e Validação ---
print("\n--- Demonstrando Espera Explícita e Validação ---")

# Espera Explícita: Aguarda uma condição específica. Mais robusta e recomendada.
try:
    # Espera até que a mensagem de sucesso (ou erro) esteja visível
    # Neste site, após o login, uma mensagem é exibida com a classe 'flash success'
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )
    print("Mensagem de flash encontrada (sucesso ou erro).")

    # Obtenção de Dados: Obtém texto visível do elemento.
    message_text = success_message.text
    print(f"Mensagem de feedback após o login: '{message_text}'")

    if "You logged into a secure area!" in message_text:
        print("Login bem-sucedido validado!")
    else:
        print("Login falhou ou mensagem inesperada.")

except Exception as e:
    print(f"Erro durante a validação da mensagem pós-login: {e}")
    driver.save_screenshot("erro_pos_login.png")

# --- Demonstração de XPath e Navegação ---
print("\n--- Demonstrando XPath e Navegação ---")

# Voltar à página de login para outra interação
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(1) # Pequena pausa para a página carregar

# Localizador por XPath: Extremamente flexível, permite navegação complexa pelo DOM.
# Usando XPath para encontrar o campo de username novamente
try:
    username_field_xpath = driver.find_element(By.XPATH, "//input[@id='username']")
    print("Elemento 'username' encontrado por XPath (com atributo ID).")
    username_field_xpath.send_keys("anotheruser")
    time.sleep(1)
    username_field_xpath.clear() # Limpa o campo de texto
    print("Campo 'username' interagido (digitou e limpou) via XPath.")

    # Encontrar o botão de logout na página de sucesso, se estiver logado
    if "secure" in driver.current_url:
        logout_button_xpath = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='button secondary radius' and contains(text(), 'Logout')]"))
        )
        print("Botão 'Logout' encontrado por XPath (com múltiplas condições e texto).")
        logout_button_xpath.click()
        print("Clicado no botão 'Logout' via XPath.")
        time.sleep(2)
        if "login" in driver.current_url:
            print("Retornou à página de login após o logout.")
except Exception as e:
    print(f"Erro ao demonstrar XPath ou logout: {e}")
    driver.save_screenshot("erro_xpath_logout.png")


print("\n--- Demonstração Concluída ---")
print("Fechando o navegador em 3 segundos...")
time.sleep(3)
driver.quit() # Fecha o navegador
print("Navegador fechado.")