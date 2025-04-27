import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import sqlite3

def create_webdriver():
    """Creates and configures the Edge WebDriver."""
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0")
    options.add_argument("--force-device-scale-factor=0.8")
    navegador = webdriver.Edge(options=options)
    navegador.maximize_window()
    return navegador

def login(navegador, username, password):
    """Logs in to the website."""
    navegador.get("https://beta.familyofficelist.org/sign-in")
    navegador.maximize_window()
    time.sleep(2)
    navegador.find_element("id", ':r0:').send_keys('admin@strategic-cap.com')
    navegador.find_element("id", ':r1:').send_keys('StrategicCapital2025#')
    navegador.find_element("xpath", '//*[@id="root"]/div[1]/div/div[1]/div/form/div[5]/button').click()
    time.sleep(4)
    navegador.get("https://beta.familyofficelist.org/my-data")

def get_total_lines(navegador):
    """Retrieves the total number of lines from the page."""
    try:
        total_linhas = WebDriverWait(navegador, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                '#simple-tabpanel-0 > div > div:nth-child(1) > div > div.MuiBox-root.css-0 > div > p.MuiTypography-root.MuiTypography-body2.css-kjrll7-root > span:nth-child(1)'))
        )
        total_linhas_texto = [total_linha.text for total_linha in total_linhas]
        return int(total_linhas_texto[0]) if total_linhas_texto else 0
    except TimeoutException:
        print("Erro ao obter o número total de linhas.")
        return 0

def extract_company_data(tr):
    """Extracts company information from a table row."""
    company = "no company"
    site = "no web site"
    office_type = "no office type"
    country = "no country"
    city = "no city"
    try:
        td_company = tr.find_element(By.XPATH, 'td[2]')
        company = td_company.find_element(By.XPATH, 'div/div/p').text
    except NoSuchElementException:
        pass
    try:
        td_site = tr.find_element(By.XPATH, 'td[3]')
        site = td_site.find_element(By.XPATH, 'span/p/a').get_attribute('href')
    except NoSuchElementException:
        pass
    try:
        td_office_type = tr.find_element(By.XPATH, 'td[4]')
        office_type = td_office_type.find_element(By.XPATH, 'p').text
    except NoSuchElementException:
        pass
    try:
        td_country = tr.find_element(By.XPATH, 'td[5]')
        country = td_country.find_element(By.XPATH, 'div/p').text
    except NoSuchElementException:
        pass
    try:
        td_city = tr.find_element(By.XPATH, 'td[6]')
        city = td_city.find_element(By.XPATH, 'p').text
    except NoSuchElementException:
        pass
    return company, site, office_type, country, city

def extract_office_details(navegador):
    """Extracts office details from the pop-up."""
    inves = 'no investors'
    company_phones = 'no phone'
    company_address = 'no address'
    try:
        offices = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                'div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper'))
        )
        try:
            investors_elements = offices.find_elements(By.CSS_SELECTOR,
                                                        'div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(1) > p')
            inves = "\n".join([investor.text for investor in investors_elements])
        except NoSuchElementException:
            pass
        try:
            phones_elements = offices.find_elements(By.CSS_SELECTOR,
                                                     'div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(2) > a')
            company_phones = "\n".join([phone.text for phone in phones_elements])
        except NoSuchElementException:
            pass
        try:
            address_elements = offices.find_elements(By.CSS_SELECTOR,
                                                       'div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(3) > a')
            company_address = "\n".join([adress.text for adress in address_elements])
        except NoSuchElementException:
            pass
        return inves, company_phones, company_address
    except TimeoutException:
        return inves, company_phones, company_address

def extract_contact_details(navegador, td):
    """Extracts contact details from the contact pop-up."""
    nomes_texto = []
    cargos_texto = []
    phones_texto = []
    emails_texto = []
    try:
        nomes = WebDriverWait(navegador, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//h3[@class="MuiTypography-root MuiTypography-h3 css-15y59ci-root"]'))
        )
        nomes_texto = [nome.text for nome in nomes]
        cargos = navegador.find_elements(By.XPATH, '//span[@class="MuiTypography-root MuiTypography-overline css-6xz56m-root"]')
        cargos_texto = [cargo.text for cargo in cargos]
        phones = navegador.find_elements(By.XPATH, '//div[@class="MuiBox-root css-0"]//a[@class="MuiTypography-root MuiTypography-body1 MuiLink-root MuiLink-underlineAlways css-1wqzc97-root"]')
        phones_texto = [phone.text for phone in phones]
        emails = td.find_elements(By.XPATH, '//a[contains(@href, "mailto")]')
        emails_texto = [email.text for email in emails]
    except (NoSuchElementException, TimeoutException):
        pass
    return nomes_texto, cargos_texto, phones_texto, emails_texto

def save_to_sqlite(data):
    """Saves the extracted data to an SQLite database."""
    conn = sqlite3.connect('my_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            count_contact INTEGER,
            company TEXT,
            website TEXT,
            office TEXT,
            investors TEXT,
            company_phones TEXT,
            company_address TEXT,
            city_company TEXT,
            country_company TEXT,
            name TEXT,
            position TEXT,
            contact_phone TEXT,
            email TEXT
        )
    ''')
    cursor.executemany('''
        INSERT INTO contacts (count_contact, company, website, office, investors, company_phones,
                             company_address, city_company, country_company, name, position, contact_phone, email)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()
    cursor.close()
    conn.close()

def process_page(navegador, conta_contatos):
    """Processes a single page of the table."""
    tabela_movimentacoes = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="table"]/tbody'))
    )
    rows = tabela_movimentacoes.find_elements(By.TAG_NAME, "tr")
    page_data = []
    for i, tr in enumerate(rows):
        try:
            td_company_click = WebDriverWait(tr, 10).until(
                EC.element_to_be_clickable((By.XPATH, 'td[2]/div/div/p'))
            )
            company, site, office_type, country, city = extract_company_data(tr)
            td_company_click.click()
            WebDriverWait(navegador, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@value='OFFICE']"))
            ).click()
            inves, company_phones, company_address = extract_office_details(navegador)
            WebDriverWait(navegador, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@value='OFFICE']"))
            ).click()
            WebDriverWait(navegador, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,
                    'body > div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-kteami-popper-popper > div > div:nth-child(3) > div:nth-child(2) > div > button:nth-child(2)'))
            ).click()
            td_contacts = WebDriverWait(tr, 10).until(EC.presence_of_element_located((By.XPATH, 'td[2]')))
            nomes, cargos, phones, emails = extract_contact_details(navegador, td_contacts)
            navegador.find_element(By.XPATH, "//span[@aria-label='Close']/button").click()

            for nome, cargo, phone, email in zip(nomes, cargos, phones, emails):
                page_data.append((conta_contatos, company, site, office_type, inves, company_phones,
                                  company_address, city, country, nome, cargo, phone, email))
                conta_contatos += 1
            print(f"Processada linha {i + 1} da página atual.")
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Erro ao processar linha {i + 1}: {e}")
            try:
                close_button = navegador.find_element(By.XPATH, "//span[@aria-label='Close']/button")
                close_button.click()
            except NoSuchElementException:
                pass
    return page_data, conta_contatos

def navigate_next_page(navegador):
    """Navigates to the next page if the button is available."""
    try:
        next_button = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                '//*[@id="simple-tabpanel-0"]/div/div[2]/div/div/nav/ul/li[7]/button'))
        )
        navegador.execute_script("arguments[0].scrollIntoView();", next_button)
        next_button.click()
        WebDriverWait(navegador, 10).until(EC.staleness_of(next_button)) # Wait for page load
        return True
    except (NoSuchElementException, TimeoutException):
        return False

if __name__ == "__main__":
    navegador = create_webdriver()
    try:
        login(navegador, 'admin@strategic-cap.com', 'StrategicCapital2025#')
        navegador.get("https://beta.familyofficelist.org/my-data")
        total_lines = get_total_lines(navegador)
        print(f"Total de linhas a serem processadas: {total_lines}")

        all_data = []
        conta_contatos = 1
        processed_count = 0

        while True:
            page_data, conta_contatos = process_page(navegador, conta_contatos)
            all_data.extend(page_data)
            processed_count += len(page_data)
            print(f"Total de contatos processados até agora: {processed_count}/{total_lines if total_lines > 0 else 'desconhecido'}")

            if total_lines > 0 and processed_count >= total_lines:
                print("Todos os contatos foram processados.")
                break

            if not navigate_next_page(navegador):
                print("Não há mais páginas para navegar.")
                break
            time.sleep(2) # Espera para a próxima página carregar

        save_to_sqlite(all_data)
        print("Dados salvos no banco de dados 'my_data.db'.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        navegador.quit()