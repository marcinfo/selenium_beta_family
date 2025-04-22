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
navegador.find_element("id", ':r0:').send_keys('admin@strategic-cap.com')
navegador.find_element("id", ':r1:').send_keys('StrategicCapital2025#')
navegador.find_element("xpath", '//*[@id="root"]/div[1]/div/div[1]/div/form/div[5]/button').click()
time.sleep(2)
navegador.get("https://beta.familyofficelist.org/my-data")
time.sleep(5)

tabela_movimentacoes = navegador.find_element("xpath", '//*[@id="table"]/tbody')

# navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
my_data = []

while True:
    for tr in tabela_movimentacoes.find_elements("tag name", "tr"):
        navegador.find_element("xpath", '//*[@id="table"]/tbody/tr[1]/td[2]/div/div/p').click()
        time.sleep(2)
        spans = navegador.find_elements(By.CSS_SELECTOR,
                                        'div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper')
        for span in spans:
            my_data.append(span.text)
            print(span.text)
        print(my_data)

navegador.quit()