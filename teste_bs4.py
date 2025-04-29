import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import sqlite3
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()

options.add_argument("--start-maximized")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0")
options.add_argument("--force-device-scale-factor=0.8")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-background-timer-throttling")

navegador = webdriver.Chrome(options=options)
navegador.maximize_window()
navegador.get("https://beta.familyofficelist.org/sign-in")

# Aqui você deve adicionar o código para realizar a autenticação
# Exemplo:
time.sleep(2)
navegador.find_element("id", ':r0:').send_keys('admin@strategic-cap.com')
navegador.find_element("id", ':r1:').send_keys('StrategicCapital2025#')
navegador.find_element("xpath", '//*[@id="root"]/div[1]/div/div[1]/div/form/div[5]/button').click()
time.sleep(4)
my_data = []
# Aguarda a página carregar após o login
navegador.get("https://beta.familyofficelist.org/my-data")

WebDriverWait(navegador, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="table"]/tbody')))
tabela_movimentacoes = navegador.find_element("xpath", '//*[@id="table"]/tbody')

# Extrai o HTML da página autenticada
html = navegador.page_source

# Usa o BeautifulSoup para analisar o HTML
soup = BeautifulSoup(html, 'html.parser')

# Exemplo de como encontrar e imprimir todos os links na página

tabela = soup.select_one('#table > tbody')
i=0
dados=[]
for linha in tabela.find_all('tr'):
    colunas = linha.find_all('td')
    dados.append([coluna.text.strip() for coluna in colunas])
    WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, f'//*[@id="table"]/tbody/tr[{i + 1}]/td[2]/div/div/p'))).click()
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@value='CONTACTS']"))).click()
    except:
        pass
    offices = navegador.find_elements(By.CSS_SELECTOR,
                                      'div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper')

    WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@value='OFFICE']"))).click()
    # Extrai o HTML do pop-up
    html_pop_up = navegador.page_source

    # Usa o BeautifulSoup para analisar o HTML do pop-up
    soup_pop_up = BeautifulSoup(html_pop_up, 'html.parser')

    elemento_pop_up = soup_pop_up.select_one('body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div')

    address = elemento_pop_up.select_one('body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(2) > a')
    try:
        phone_company = elemento_pop_up.select_one('body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(2) > a').text
    except NoSuchElementException:
        phone_company = 'no phone'
    investor_type = elemento_pop_up.select_one('body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(1) > p')
    descripition = []
    try:
        read_more = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(3) > div > div > h4'))
        )
        # Clica no elemento
        try:
            read_more.click()
        except :
            pass

        company_descriptions = navegador.find_elements(By.CSS_SELECTOR,
                                                       'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(3) > div > div > div > div')
        company_descriptions_texto = [company_description.text for company_description in company_descriptions]

        for p in company_descriptions:
            descripition.append(p.text)
    except:
        descripition='no description'
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@value='OFFICE']"))).click()
    except:
        pass
    spans = navegador.find_elements(By.CSS_SELECTOR,
                                    'div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper')
    WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(2) > div > button:nth-child(2)'))).click()
    try:
        name = navegador.find_element(By.XPATH,
                                       '//h3[@class="MuiTypography-root MuiTypography-h3 css-15y59ci-root"]')

        nomes_texto = [nome.text for nome in navegador.find_elements(By.TAG_NAME, 'h3')]

        cargos = navegador.find_elements(By.XPATH,
                                         '//span[@class="MuiTypography-root MuiTypography-overline css-6xz56m-root"]')

        phones = navegador.find_elements(By.XPATH,
                                         '//div[@class="MuiBox-root css-0"]//a[@class="MuiTypography-root MuiTypography-body1 MuiLink-root MuiLink-underlineAlways css-1wqzc97-root"]')

        emails = navegador.find_elements(By.XPATH, '//a[contains(@href, "mailto")]')
    except NoSuchElementException:
        navegador.find_element(By.XPATH, "//span[@aria-label='Close']/button").click()
        name = "sem nome"
        nomes_texto = []
        cargos = []
        phones = []
        emails = []
    except (NoSuchElementException, TimeoutException):
        navegador.find_element(By.XPATH, "//span[@aria-label='Close']/button").click()
        continue
    cargos_texto = [cargo.text for cargo in cargos]
    phones_texto = [phone.text for phone in phones]
    emails_texto = [email.text for email in emails]

    for nome, cargo, phone, email in zip(nomes_texto, cargos_texto, phones_texto, emails_texto):
        print(i,nome,cargos_texto,phones_texto,emails_texto)

    address_texto = address.text
    investor_type_texto = investor_type.text
    navegador.find_element(By.XPATH, "//span[@aria-label='Close']/button").click()

    i=i+1

# Fecha o navegador
navegador.quit()
