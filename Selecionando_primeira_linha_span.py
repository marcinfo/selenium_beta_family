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
time.sleep(2)

tabela_movimentacoes = navegador.find_element("xpath", '//*[@id="table"]/tbody')

my_data = []

while True:
    for tr in tabela_movimentacoes.find_elements("tag name", "tr"):

        active_element = navegador.execute_script("return document.activeElement")

        # Verifique se o elemento ativo é uma <div>
        if active_element.tag_name == 'div':
           print("A div ativa é:", active_element.get_attribute('outerHTML'))
        else:
            print("O elemento ativo não é uma div. É um:", active_element.tag_name)

        # Feche o driver após a interação

        navegador.find_element("xpath", '//*[@id="table"]/tbody/tr[1]/td[2]/div/div/p').click()
        time.sleep(1)
        spans = navegador.find_elements(By.CSS_SELECTOR,
                                        'div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper')
        time.sleep(1)

        navegador.find_element(By.CSS_SELECTOR, 'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(2) > div > button:nth-child(2)').click()
        for span in spans:
            a_tags = span.find_elements(By.TAG_NAME, 'a')
            p_tags = span.find_elements(By.TAG_NAME, 'p')
            h3_tags = span.find_elements(By.TAG_NAME, 'h3')
            h2_tags = span.find_elements(By.TAG_NAME, 'h2')
            spaner = span.find_elements(By.TAG_NAME, 'span')
            for tag in h3_tags + spaner + a_tags + p_tags + h2_tags :
                my_data.append(tag.text)

        navegador.find_element(By.XPATH, "//span[@aria-label='Close']/button").click()
        time.sleep(1)
        navegador.find_element(By.XPATH, '//*[@id="table"]/tbody/tr[1]/td[1]').click()
        if active_element.tag_name == 'div':
           print("A div ativa é:", active_element.get_attribute('outerHTML'))
        else:
            print("O elemento ativo não é uma div. É um:", active_element.tag_name)

        print(my_data)
    time.sleep(50)
navegador.quit()