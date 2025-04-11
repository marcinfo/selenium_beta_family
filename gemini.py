
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
import  pandas as pd
import time
from bs4 import BeautifulSoup
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
tabela_my_data = navegador.find_element("xpath",'//*[@id="table"]/tbody')
htmlContent = tabela_my_data.get_attribute('outerHTML')
soup = BeautifulSoup(htmlContent, 'html.parser')
dados  = soup.find(name='tbody').find_all(name='tr')
print (dados)
tabela_movimentacoes= navegador.find_element("xpath",'//*[@id="table"]/tbody')
time.sleep(5)