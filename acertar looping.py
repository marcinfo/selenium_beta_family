import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
import time
navegador = webdriver.Chrome()
navegador.get("https://beta.familyofficelist.org/sign-in")
navegador.maximize_window()
time.sleep(2)
navegador.find_element("id",':r0:').send_keys('admin@strategic-cap.com')
navegador.find_element("id",':r1:').send_keys('StrategicCapital2025#')
navegador.find_element("xpath",'//*[@id="root"]/div[1]/div/div[1]/div/form/div[5]/button').click()
time.sleep(2)
navegador.get("https://beta.familyofficelist.org/my-data")
time.sleep(5)

tabela_movimentacoes= navegador.find_element("xpath",'//*[@id="table"]/tbody')
spans = navegador.find_elements(By.CSS_SELECTOR,
                                        'div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper')
#navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
my_data = []
while True:
    for tr in tabela_movimentacoes.find_elements("tag name", "tr"):

        for td in tabela_movimentacoes.find_elements("tag name", "td"):
            print(td.text)
            navegador.find_element("xpath", '//*[@id="table"]/tbody/tr[1]/td[2]/div/div/p').click()
            time.sleep(5)
            navegador.find_element(By.XPATH, "//button[@value='CONTACTS']").click()
            time.sleep(15)
            navegador.find_element(By.XPATH, "//span[@aria-label='Close']/button").click()

            break
            print(td.text)
        navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        try:
            navegador.find_element("xpath", '//*[@id="simple-tabpanel-0"]/div/div[2]/div/div/nav/ul/li[7]/button').click()
        except:
            break
df_my_data = pd.DataFrame(my_data)
print(my_data)
time.sleep(50)
navegador.quit()


