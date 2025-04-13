import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

navegador = webdriver.Chrome()
navegador.get("https://beta.familyofficelist.org/sign-in")
navegador.maximize_window()
time.sleep(2)
navegador.find_element("id", ':r0:').send_keys('admin@strategic-cap.com')
navegador.find_element("id", ':r1:').send_keys('StrategicCapital2025#')
navegador.find_element("xpath", '//*[@id="root"]/div[1]/div/div[1]/div/form/div[5]/button').click()
time.sleep(2)
navegador.get("https://beta.familyofficelist.org/my-data")

WebDriverWait(navegador, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="table"]/tbody')))
tabela_movimentacoes = navegador.find_element("xpath", '//*[@id="table"]/tbody')

my_data = []
i = 0

while True:
    for tr in tabela_movimentacoes.find_elements(By.TAG_NAME, "tr"):
        print(tr.text)
        try:
            WebDriverWait(navegador, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'//*[@id="table"]/tbody/tr[{i + 1}]/td[2]/div/div/p'))).click()
            spans = navegador.find_elements(By.CSS_SELECTOR,
                                            'div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper')
            try:
                WebDriverWait(navegador, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@value='CONTACTS']"))).click()
                time.sleep(1)

                navegador.find_element(By.CSS_SELECTOR,
                                       'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(2) > div > button:nth-child(2)').click()

                i += 1
            except:
                pass
            for span in spans:
                a_tags = span.find_elements(By.TAG_NAME, 'a')
                p_tags = span.find_elements(By.TAG_NAME, 'p')
                h3_tags = span.find_elements(By.TAG_NAME, 'h3')
                h2_tags = span.find_elements(By.TAG_NAME, 'h2')
                spaner = span.find_elements(By.TAG_NAME, 'span')
                for tag in h3_tags + spaner + a_tags + p_tags + h2_tags:
                    print(tag.text)
                    my_data.append(tag.text)
            WebDriverWait(navegador, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='Close']/button"))).click()
        except:
            print(f"Elemento na linha {i+1} não encontrado.")

        navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            WebDriverWait(navegador, 10).until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="simple-tabpanel-0"]/div/div[2]/div/div/nav/ul/li[7]/button'))).click()
        except:
            break

df_my_data = pd.DataFrame(my_data)
print(my_data)
time.sleep(50)
navegador.quit()
