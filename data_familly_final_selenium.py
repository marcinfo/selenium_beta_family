#bibliotecas utilizadas para o Danco de Dados
import sqlite3
#biblioteca para manioulação do sistema
import sys
" bibliotecas para datas"
import time
from datetime import datetime
#Bibliotecas para controle do navegador e extração dos dados
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()

# Para definir o user-agent corretamente:
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0")

# Para iniciar o navegador
navegador = webdriver.Firefox(options=options)

# Maximizar a janela após iniciar
navegador.maximize_window()

#inicia o site
navegador.get("https://beta.familyofficelist.org/sign-in")

time.sleep(2)
#faz o login
navegador.find_element("id", ':r0:').send_keys('admin@strategic-cap.com')
navegador.find_element("id", ':r1:').send_keys('StrategicCapital2025#')
navegador.find_element("xpath", '//*[@id="root"]/div[1]/div/div[1]/div/form/div[5]/button').click()
time.sleep(4)
#acessa a pagina my-data
navegador.get("https://beta.familyofficelist.org/my-data")
#acessa a tabela
WebDriverWait(navegador, 1000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="table"]/tbody')))
#coloca a tabela em uma variavel
tabela_movimentacoes = navegador.find_element("xpath", '//*[@id="table"]/tbody')
#parametros
my_data = []
i = 0
conta_corp=0
total_contacts = navegador.find_elements(By.CSS_SELECTOR,'#simple-tabpanel-0 > div > div:nth-child(1) > div > div.MuiBox-root.css-0 > div > p.MuiTypography-root.MuiTypography-body2.css-kjrll7-root > span:nth-child(2)')
total_contacts_texto = [total_linha.text for total_linha in total_contacts]
total = int(total_contacts_texto[0])
conta_contatos=0
not_save =0
now = datetime.now()
current_time = now.strftime("%d-%m-%Y %H:%M:%S")
#time.sleep(2)
while True:
    #Percorre as paginas da tabela
    for tr in tabela_movimentacoes.find_elements(By.TAG_NAME, "tr"):
        #Percorre as linhas da tabela
        for td in tr.find_elements(By.TAG_NAME, "td"):
            td = tr.find_element(By.XPATH, 'td[2]')
            # Localiza o elemento da empresa dentro da célula
            td_company = tr.find_element(By.XPATH, 'td[2]')
            company = td_company.find_element(By.XPATH, 'div/div/p').text
            #tenta extrair o site
            try:
                td_site = tr.find_element(By.XPATH, 'td[3]')
                site = td_site.find_element(By.XPATH, 'span/p/a').get_attribute('href')
            except:
                site = "no web site"
            #tenta extrair o office_type
            try:
                td_office_type = tr.find_element(By.XPATH, 'td[4]')
                td_office = td_office_type.find_element(By.XPATH, 'p').text
            except:
                td_office = "no office type"
            #Tenta extrair o country
            try:
                td_country = tr.find_element(By.XPATH, 'td[5]')
                country = td_country.find_element(By.XPATH, 'div/p').text
            except:
                country = "no country"
            #tenta extrair city
            try:
                td_city = tr.find_element(By.XPATH, 'td[6]')
                city = td_city.find_element(By.XPATH, 'p').text
            except:
                city = "no city"
        try:
            #clica na tabela para acessar o poup up
            WebDriverWait(navegador, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'//*[@id="table"]/tbody/tr[{i + 1}]/td[2]/div/div/p'))).click()
            #ativa div
            offices = navegador.find_elements(By.CSS_SELECTOR,
                                              'div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper')
            try:
                offices.click()
            except:
                pass
            #clica nbo botão Office
            try:
                WebDriverWait(navegador, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@value='OFFICE']"))).click()
            except:
                pass
            #pegar dados da aba Office
            for office in offices:
                company_name = office.find_element(By.CSS_SELECTOR,
                                                   'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(1) > h2').text

                try:
                    investors = navegador.find_elements(By.CSS_SELECTOR,
                                                        'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(1) > p')
                    investors_texto = [investor.text for investor in investors]
                    inves = "\n".join(investors_texto)
                except:
                    inves = 'no investors'
                try:
                    phones = navegador.find_elements(By.CSS_SELECTOR,
                                                     'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(2) > a')
                    phones_texto = [phone.text for phone in phones]
                    company_phones = "\n".join(phones_texto)
                except:
                    company_phones = 'no phone'
                try:
                    addresses = navegador.find_elements(By.CSS_SELECTOR,
                                                       'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(3) > a')

                    addresses_texto = [address.text.replace('\n', ' ') for address in addresses]# Remove quebras de linha
                    company_address = " ".join(addresses_texto)
                except:
                    company_address = 'no address'
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
                name1 = navegador.find_element(By.XPATH,
                                               '//h3[@class="MuiTypography-root MuiTypography-h3 css-15y59ci-root"]')
                nomes_texto = [nome.text for nome in navegador.find_elements(By.TAG_NAME, 'h3')]
                cargos = navegador.find_elements(By.XPATH,
                                                 '//span[@class="MuiTypography-root MuiTypography-overline css-6xz56m-root"]')
                phones = navegador.find_elements(By.XPATH,
                                                 '//div[@class="MuiBox-root css-0"]//a[@class="MuiTypography-root MuiTypography-body1 MuiLink-root MuiLink-underlineAlways css-1wqzc97-root"]')
                emails = td.find_elements(By.XPATH, '//a[contains(@href, "mailto")]')
            except NoSuchElementException:
                navegador.find_element(By.XPATH, "//span[@aria-label='Close']/button").click()
                name1 = "sem nome"
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
            verifica_salvar=0
            for nome, cargo, phone, email in zip(nomes_texto, cargos_texto, phones_texto, emails_texto):
                conn = sqlite3.connect('my_data.db')
                cursor = conn.cursor()
                # Verifica se o registro já existe
                cursor.execute('''
                                        SELECT COUNT(*) FROM contacts WHERE company = ? AND website = ? AND office = ? AND investors = ? AND\
                                           company_phones = ? AND company_address = ? AND city_company = ? AND country_company = ? AND name = ? AND position = ? AND contact_phone = ? AND email = ?
                                    ''', (company,site, td_office, inves,company_phones, company_address, city, country,   nome, cargo, phone, email))
                result = cursor.fetchone()
                if result[0] > 0:
                    print(f"Dados não inseridos para {company} {nome}, {cargo}, {phone}, {email} - já existem no banco de dados.")
                    not_save=not_save+1
                    conta_contatos = conta_contatos + 1
                    try:
                        cursor.close()
                        conn.close()
                    except:
                        pass
                    if not_save >= 2000 and i == 2000:
                        print('Os 20 primeiros contatos foram salvos anteriormente, o script vai ser fechado')
                        navegador.quit()
                        sys.exit()
                else:
                    cursor.execute('''
                                        INSERT OR IGNORE INTO contacts (date_extract,company, website, office,investors,company_phones,\
                                         company_address,city_company, country_company, name, position, contact_phone, email)
                                            VALUES (?,?,?,?,?, ?, ?, ?, ?, ?, ?, ?, ?)
                                                ''',
                               (current_time,company, site, td_office, inves, company_phones,
                                company_address, city, country, nome, cargo, phone, email))
                    conta_contatos = conta_contatos + 1
                    conn.commit()  # Corrigido de 'comit' para 'commit'
                    print(f"Dados inseridos no banco de dados.")
                    cursor.close()
                    conn.close()
                    not_save=0
                # Adicionado
            navegador.find_element(By.XPATH, "//span[@aria-label='Close']/button").click()
            i += 1
            conta_corp = conta_corp + 1
            print(f"total de copntatoc processados {conta_contatos}, de {total} linha atual {i} iteração {conta_corp}.", )
            if i == 100:
                i = 0
                navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                navegador.find_element("xpath",
                                       '//*[@id="simple-tabpanel-0"]/div/div[2]/div/div/nav/ul/li[7]/button').click()
        except:
            print("finalizando script")
            #sys.exit()
            #print(f"Elemento na linha {i + 1} não encontrado.")
"""df = pd.DataFrame(my_data)
# Exporta o DataFrame para um arquivo CSV
csv_file = "page5.csv"
df.to_csv(csv_file, index=False)
break"""

navegador.quit()
