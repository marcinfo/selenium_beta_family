import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
import sqlite3

options = webdriver.EdgeOptions()
options.add_argument("--start-maximized")

options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0")
options.add_argument("--force-device-scale-factor=0.8")
navegador = webdriver.Edge(options=options)
navegador.maximize_window()

navegador.get("https://beta.familyofficelist.org/sign-in")

time.sleep(2)
navegador.find_element("id", ':r0:').send_keys('admin@strategic-cap.com')
navegador.find_element("id", ':r1:').send_keys('StrategicCapital2025#')
navegador.find_element("xpath", '//*[@id="root"]/div[1]/div/div[1]/div/form/div[5]/button').click()
time.sleep(2)

navegador.get("https://beta.familyofficelist.org/my-data")
time.sleep(2)

tabela_movimentacoes = navegador.find_element("xpath", '//*[@id="table"]/tbody')

my_data = []
i = 0

conta_corp=0
total_linhas = navegador.find_elements(By.CSS_SELECTOR,'#simple-tabpanel-0 > div > div:nth-child(1) > div > div.MuiBox-root.css-0 > div > p.MuiTypography-root.MuiTypography-body2.css-kjrll7-root > span:nth-child(1)')
total_linhas_texto = [total_linha.text for total_linha in total_linhas]
total = int(total_linhas_texto[0])
print(total)
time.sleep(20)
# Conectar ao banco de dados
"""conn = sqlite3.connect('my_data.db')
cursor = conn.cursor()"""
# Criar tabela se não existir
"""cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    cargo TEXT,
    phone TEXT,
    email TEXT
)
''')"""


while True:
    for tr in tabela_movimentacoes.find_elements("tag name", "tr"):
        try:
            navegador.find_elements(By.CSS_SELECTOR,
                                    'div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper')

        except:
            pass
        for td in tr.find_elements(By.TAG_NAME, "td"):
            try:
                tentativa = 0
                WebDriverWait(navegador, 10).until(
                    EC.element_to_be_clickable((By.XPATH, f'//*[@id="table"]/tbody/tr[{i + 1}]/td[2]/div/div/p'))).click()
                time.sleep(1)
                offices = navegador.find_elements(By.CSS_SELECTOR,
                                                'div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper')
                try:
                    office.click()
                except:
                    pass
                for office in offices:
                    company_name = office.find_element(By.CSS_SELECTOR, 'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(1) > h2').text
                    """if i == 0:
                        time.sleep(0.5)"""

                    try:
                        web_sites = navegador.find_elements(By.CSS_SELECTOR,'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1) > a')
                        web_sites_texto = [web_site.text for web_site in web_sites]
                        web = "\n".join(web_sites_texto)
                    except:
                        web='no web site'
                    try:
                        investors = navegador.find_elements(By.CSS_SELECTOR,'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(1) > p')
                        investors_texto = [investor.text for investor in investors]
                        inves = "\n".join(investors_texto)
                    except:
                        inves='no investors'

                    try:
                        phones = navegador.find_elements(By.CSS_SELECTOR,'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(2) > a')
                        phones_texto = [phone.text for phone in phones]
                        fone = "\n".join(phones_texto)
                    except:
                        fone='no phone'
                    try:
                        adresses = navegador.find_elements(By.CSS_SELECTOR,'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(2) > a')
                        adresses_texto = [adress.text for adress in adresses]
                        endereco = "\n".join(adresses_texto)
                    except:
                        endereco='no address'
                    try:
                        office_types = navegador.find_elements(By.CSS_SELECTOR,'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(2) > p')
                        office_types_texto = [office_types.text for office_types in office_types]
                    except:
                        office_types_texto='no office type'
                    try:
                        company_descriptions = navegador.find_elements(By.CSS_SELECTOR,'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(3) > div > div > div > div')
                        company_descriptions_texto = [company_description.text for company_description in company_descriptions]
                    except (NoSuchElementException, TimeoutException):
                        company_descriptions_texto='no description'
                    try:
                        descripition = []
                        read_more = WebDriverWait(navegador, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(3) > div > div > h4'))
                        )
                         # Clica no elemento

                        read_more.click()
                        for p in company_descriptions:
                            descripit= "\n".join(p.text)
                    except (NoSuchElementException, TimeoutException):
                        for p in company_descriptions:
                            descripit = "\n".join(p.text)

                    try:
                        target_geographies = navegador.find_elements(By.CSS_SELECTOR,'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(5) > div > div:nth-child(1) > div:nth-child(1) > p')
                        target_geographies_texto = [target_geographie.text for target_geographie in target_geographies]
                    except:
                        target_geographies_texto ='no target geographies'
                    try:
                        deal_structures = navegador.find_elements(By.CSS_SELECTOR,'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(5) > div > div:nth-child(1) > div:nth-child(2)')
                        deal=[]
                        for p_deal in deal_structures:
                            deal.append(p_deal.text)
                        deals = "\n".join(deal)
                    except:
                        deals=['no deal']

                    try:
                        industry_Focus = navegador.find_elements(By.CSS_SELECTOR,'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(5) > div > div:nth-child(2) > div:nth-child(1)')
                        industry = []
                        for p_industry in industry_Focus:
                            industry.append(p_industry.text)
                        #industrie = "\n".join(industry)
                    except:
                        industry=['no industries']

                    try:
                        sub_industry = navegador.find_elements(By.CSS_SELECTOR,'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(5) > div > div:nth-child(2) > div:nth-child(2)')
                        sub = []
                        for p_sub_industry  in sub_industry :
                            sub.append(p_sub_industry.text)
                        sub_industrie = "\n".join(sub)
                    except:
                        sub_industrie=['no sub industrie']

                    try:

                        WebDriverWait(navegador, 10).until(
                            EC.element_to_be_clickable((By.XPATH, "//button[@value='OFFICE']"))).click()
                    except:
                        pass
                    WebDriverWait(navegador, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                    'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(2) > div > button:nth-child(2)'))).click()
                    try:
                        contact_names = navegador.find_elements(By.CSS_SELECTOR,'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div:nth-child(1) > div.MuiBox-root.css-0 > h3')
                        nome= [nome.text for nome in contact_names]
                        positions = navegador.find_elements(By.CSS_SELECTOR,'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div:nth-child(1) > div.MuiBox-root.css-0 > span')

                        contact_phones = navegador.find_elements(By.CSS_SELECTOR,'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div:nth-child(2) > a')

                        e_mails = navegador.find_elements(By.CSS_SELECTOR,'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div:nth-child(3) > a')

                        navegador.find_element(By.XPATH, "//span[@aria-label='Close']/button").click()
                    except NoSuchElementException:
                        navegador.find_element(By.XPATH, "//span[@aria-label='Close']/button").click()
                        nome = ['no contact']
                        positions = ['no positions']
                        contact_phones = ['no contact phone']
                        e_mails = ['no e-mail']
                    except (NoSuchElementException, TimeoutException):
                        navegador.find_element(By.XPATH, "//span[@aria-label='Close']/button").click()
                        continue

                    contact_name_texto = [contact_name.text for contact_name in contact_names]
                    position_texto = [position.text for position in positions]
                    contact_phones_texto = [contact_phone.text for contact_phone in contact_phones]

                    e_mail_texto = [e_mail.text for e_mail in e_mails]
                    x=0
                    for x, (nome, cargo, phone, email) in enumerate(
                            zip(contact_name_texto, position_texto, contact_phones_texto,e_mail_texto)):
                        conn = sqlite3.connect('my_data.db')
                        cursor = conn.cursor()
                        cursor.execute('''
                                INSERT INTO contacts (nome, cargo, phone, email)
                                VALUES (?, ?, ?, ?)
                            ''', (nome, cargo, phone, email))
                        conn.commit()  # Corrigido de 'comit' para 'commit'
                        cursor.close()
                        conn.close()  # Adicionado para fechar a conexão com o banco de dados

                    i = i + 1
                    conta_corp = conta_corp + 1
                    print(f"total processada {conta_corp}, de {total} linha atual {i}  ", )

                    #print(my_data)
                    if i==100:
                        i = 0
                        navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        navegador.find_element("xpath",
                                               '//*[@id="simple-tabpanel-0"]/div/div[2]/div/div/nav/ul/li[7]/button').click()
                        time.sleep(1)
                    elif conta_corp == 4982:
                        df = pd.DataFrame(my_data)
                        df = df.replace('\n', ' ', regex=True)
                        # Exporta o DataFrame para um arquivo CSV
                        csv_file = "completo.csv"
                        df.to_csv(csv_file, index=False)
            except:
                print(f"Elemento na linha {i + 1} não encontrado.")
                tentativa = tentativa + 1
                print('tentativa ',tentativa)
                continue

            #print(my_data)

navegador.quit()