import pandas as pd
import requests
from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Your User-Agent'
}

url = 'https://pt.wikipedia.org/wiki/Lista_de_presidentes_do_Brasil'
req = requests.get(url, headers=header)
html = BeautifulSoup(req.text, 'html.parser')

soup = html.find_all('ol', attrs={'class': not 'references'})

dados = []

for s in soup:
    dados.append(s.text.split('\n'))

nome_periodo = [(a.split('(')[0].strip(), a.split('(')[1].strip(')')) for i in dados for a in i]

df_presidentes_bra = pd.DataFrame(nome_periodo, columns=['Presidentes do Brasil', 'Período'])
print(df_presidentes_bra)
