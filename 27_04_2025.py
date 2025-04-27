import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

options = webdriver.EdgeOptions()
options.add_argument("--start-maximized")

options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0")
options.add_argument("--force-device-scale-factor=0.8")
navegador = webdriver.Edge(options=options)
navegador.maximize_window()

navegador.get("https://beta.familyofficelist.org/sign-in")
navegador.maximize_window()
time.sleep(2)
navegador.find_element("id", ':r0:').send_keys('admin@strategic-cap.com')
navegador.find_element("id", ':r1:').send_keys('StrategicCapital2025#')
navegador.find_element("xpath", '//*[@id="root"]/div[1]/div/div[1]/div/form/div[5]/button').click()
time.sleep(4)
navegador.get("https://beta.familyofficelist.org/my-data")

WebDriverWait(navegador, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="table"]/tbody')))
tabela_movimentacoes = navegador.find_element("xpath", '//*[@id="table"]/tbody')
# time.sleep(30)
my_data = []
i = 0
#time.sleep(60)
while True:
    for tr in tabela_movimentacoes.find_elements(By.TAG_NAME, "tr"):
        for td in tr.find_elements(By.TAG_NAME, "td"):
            td = tr.find_element(By.XPATH, 'td[2]')
            # Localiza o elemento da empresa dentro da célula

            td_company = tr.find_element(By.XPATH, 'td[2]')
            company = td_company.find_element(By.XPATH, 'div/div/p').text
            try:
                td_site = tr.find_element(By.XPATH, 'td[3]')
                site = td_site.find_element(By.XPATH, 'span/p/a').get_attribute('href')
            except:
                site = "no web site"

            try:
                td_office_type = tr.find_element(By.XPATH, 'td[4]')
                office = td_office = td_office_type.find_element(By.XPATH, 'p').text
            except:
                office = "no office type"
            try:
                td_country = tr.find_element(By.XPATH, 'td[5]')
                country = td_country.find_element(By.XPATH, 'div/p').text
            except:
                country = "no country"

            try:
                td_city = tr.find_element(By.XPATH, 'td[6]')
                city = td_city.find_element(By.XPATH, 'p').text
            except:
                city = "no city"

        try:
            WebDriverWait(navegador, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'//*[@id="table"]/tbody/tr[{i + 1}]/td[2]/div/div/p'))).click()
            time.sleep(1)
            offices = navegador.find_elements(By.CSS_SELECTOR,
                                              'div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper')
            try:
                offices.click()
            except:
                pass
            try:

                WebDriverWait(navegador, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@value='OFFICE']"))).click()
            except:
                pass
            for office in offices:
                company_name = office.find_element(By.CSS_SELECTOR,
                                                   'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(1) > h2').text
                print(company_name)
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

            dados = [{"nome": nome, "cargo": cargo, "phone": phone, "e-mail": email} for nome, cargo, phone, email in
                     zip(nomes_texto, cargos_texto, phones_texto, emails_texto)]
            """dados_com_phones = [{"id": i, "nome": nome, "cargo": cargo, "phone": phone} for i, (nome, cargo, phone) in
                               enumerate(zip(nomes_texto, cargos_texto, phones_texto), start=1)]"""

            for nome, cargo, phone, email in zip(nomes_texto, cargos_texto, phones_texto, emails_texto):
                my_data.append(
                    {"company": company, "web site": site, "office Type": office, "country": country, "city": city, \
                     "contact": nome, "position": cargo, "phone": phone, "e-mail": email})

            """for dado in dados:
                print(f"Nome: {dado['nome']}, Cargo: {dado['cargo']}")"""

            navegador.find_element(By.XPATH, "//span[@aria-label='Close']/button").click()
            i += 1
            print(i)
            if i == 100:
                i = 0
                navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                navegador.find_element("xpath",
                                       '//*[@id="simple-tabpanel-0"]/div/div[2]/div/div/nav/ul/li[7]/button').click()
                time.sleep(1)

        except:
            print(f"Elemento na linha {i + 1} não encontrado.")

            df = pd.DataFrame(my_data)
            # Exporta o DataFrame para um arquivo CSV
            csv_file = "page5.csv"
            df.to_csv(csv_file, index=False)
            break

    # navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print(my_data)

navegador.quit()
