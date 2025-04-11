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

"""pesquisa = navegador.find_element("xpath",'//*[@id="simple-tabpanel-0"]/div/div[2]/div/div/div/div/div')
seleciona_doc = Select(pesquisa)
seleciona_doc.select_by_value('1000')
navegador.execute_script("window.scroll({ top: 0, left: 0, behavior: 'smooth' });")
time.sleep(5)"""

tabela_movimentacoes= navegador.find_element("xpath",'//*[@id="table"]/tbody')


#navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
my_data = []

while True:
    for tr in tabela_movimentacoes.find_elements("tag name", "tr"):

        for td in tabela_movimentacoes.find_elements("tag name", "td"):


            my_data.append(td.text)
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


