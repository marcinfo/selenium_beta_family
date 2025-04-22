import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions as EC

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
        offices = navegador.find_elements(By.CSS_SELECTOR,
                                        'div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper')
        for office in offices:

            company_name = office.find_element("xpath", '//*[@id="table"]/tbody/tr[1]/td[2]/div/div/p').text

            web_sites = navegador.find_elements(By.CSS_SELECTOR,'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1) > a')
            web_sites_texto = [web_site.text for web_site in web_sites]

            investors = navegador.find_elements(By.CSS_SELECTOR,'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(1) > p')
            investors_texto = [cargo.text for cargo in investors]

            try:
                phones = navegador.find_elements(By.CSS_SELECTOR,'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(2) > a')
                phones_texto = [phone.text for phone in phones]
            except:
                phones_texto=''
            adresses = navegador.find_elements(By.CSS_SELECTOR,'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(3) > a')
            adresses_texto = [adress.text for adress in adresses]

            office_types = navegador.find_elements(By.CSS_SELECTOR,'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(2) > p')
            office_types_texto = [office_types.text for office_types in office_types]

            company_descriptions = navegador.find_elements(By.CSS_SELECTOR,'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(3) > div > div > div > div')

            company_descriptions_texto = [company_description.text for company_description in company_descriptions]
            descripition = []

            read_more = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(3) > div > div > h4'))
            )

             # Clica no elemento
            read_more.click()

            for p in company_descriptions:
                descripition.append(p.text)
                print(descripition)
            target_geographies = navegador.find_elements(By.CSS_SELECTOR,'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(5) > div > div:nth-child(1) > div:nth-child(1) > p')
            target_geographies_texto = [target_geographie.text for target_geographie in target_geographies]

            print(company_name,web_sites_texto,investors_texto,phones_texto,adresses_texto,office_types_texto,company_descriptions_texto,target_geographies_texto)
            time.sleep(10)
        #print(my_data)

navegador.quit()