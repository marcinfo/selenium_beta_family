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
#time.sleep(30)
my_data = []
i = 0
#time.sleep(60)
while True:
    for tr in tabela_movimentacoes.find_elements(By.TAG_NAME, "tr"):
        for td in tr.find_elements(By.TAG_NAME, "td"):
            pass
        try:
            WebDriverWait(navegador, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'//*[@id="table"]/tbody/tr[{i + 1}]/td[2]/div/div/p'))).click()
            spans = navegador.find_elements(By.CSS_SELECTOR,
                                            'div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper')
            WebDriverWait(navegador, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,
                                            'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(2) > div > button:nth-child(2)'))).click()
            for span in spans:
                name1 = navegador.find_element(By.XPATH,
                                                   '//h3[@class="MuiTypography-root MuiTypography-h3 css-15y59ci-root"]')
                cargo1 = navegador.find_element(By.XPATH,'//span[@class="MuiTypography-root MuiTypography-overline css-6xz56m-root"]')
                try:
                    name2 = navegador.find_element(By.XPATH,
                                                   '//h3[@class="MuiTypography-root MuiTypography-h3 css-15y59ci-root"]')
                    cargo2 = navegador.find_element(By.XPATH,
                                                   '//span[@class="MuiTypography-root MuiTypography-overline css-6xz56m-root"]')
                    phone2 = navegador.find_element(By.XPATH,'//a[@class="MuiTypography-root MuiTypography-body1 MuiLink-root MuiLink-underlineAlways css-1wqzc97-root"]')
                except:
                    pass
                nome1=name1.text
                cargo1=cargo1.text
                nome2 = name2.text
                cargo2 = cargo2.text
                fone2 = phone2.text

                print( nome1,nome2)




            navegador.find_element(By.XPATH, "//span[@aria-label='Close']/button").click()
            i += 1
            print(i)

        except:
            print(f"Elemento na linha {i+1} não encontrado.")
            if i >= 1000:
                pd.DataFrame(my_data, columns=["Dados"]).to_csv('arquivo.csv', index=False)
                WebDriverWait(navegador, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="simple-tabpanel-0"]/div/div[2]/div/div/nav/ul/li[7]/button'))).click()
                i = 0
    #navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print(my_data)
time.sleep(50)
navegador.quit()
