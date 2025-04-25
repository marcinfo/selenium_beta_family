import pandas as pd
import requests
from Demos.win32ts_logoff_disconnected import session
from bs4 import BeautifulSoup


login_url = "https://beta.familyofficelist.org/sign-in"

session= requests.Session()
login_page = session.get(login_url)
soup =BeautifulSoup(login_page.text,'html.parser')

crf_token = soup.find(
    name='imput',
    attrs=
)


pagina =requests.get("https://beta.familyofficelist.org/my-data")
dados_pagina = BeautifulSoup(pagina.text, 'html.parser')
WebDriverWait(navegador, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="table"]/tbody')))
todos_links = dados_pagina.find_all('a', href=True)
print(dados_pagina)

