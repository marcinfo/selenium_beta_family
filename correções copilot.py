from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializa o driver
navegador = webdriver.Chrome()

# Abre a página
navegador.get("URL_DA_SUA_TABELA")

# Aguarda até que a tabela esteja visível
WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="table"]/tbody')))

# Encontra todos os itens na tabela


# Itera sobre os itens
for i in range(len(itens)):
    try:
        tr = itens[i]
        for td in tr.find_elements(By.TAG_NAME, "td"):
            print(td.text)
            td.find_element(By.XPATH, '//*[@id="table"]/tbody/tr[1]/td[2]/div/div/p').click()  # Ajuste para clicar no item atual
            time.sleep(5)
            try:
                navegador.find_element(By.XPATH, "//button[@value='CONTACTS']").click()
            except:
                pass
            time.sleep(15)
            navegador.find_element(By.XPATH, "//span[@aria-label='Close']/button").click()

            print(td.text)
        navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        try:
            navegador.find_element(By.XPATH,
                                   '//*[@id="simple-tabpanel-0"]/div/div[2]/div/div/nav/ul/li[7]/button').click()
        except:
            break

        # Atualiza a lista de itens para garantir que o próximo item seja processado
        tabela_movimentacoes = navegador.find_element(By.XPATH, '//*[@id="table"]/tbody')
        itens = tabela_movimentacoes.find_elements(By.TAG_NAME, "tr")
    except Exception as e:
        print(f"Erro ao processar o item {i}: {e}")

# Fecha o driver
navegador.quit()
