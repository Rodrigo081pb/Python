import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pyautogui as py
import pyperclip

from datetime import date, timedelta
import time
import os
import pandas as pd
from itertools import product

# Definição de variáveis principais

Dominio = 'https://ibjjf.com'
URL = f'{Dominio}/2024-athletes-ranking' # URL alvo para scraping
HEADERS = {'USER-Agent': 'Mozilla/5.0'} # Cabeçalhos HTTP para a requisição (user-agent para se passar por um navegador)
PARAMETERS = {
'utf8': '✓',
'filters[s]': 'ranking-geral-gi',
'filters[gender]': 'male',
'filters[belt]': 'black',
'filters[weight]': 'None',
'page': 1
} # Parâmetros da query string para a requisição HTTP

def get_page_content(url, headers, parameters): # Faz uma requisição GET à URL com os headers e parâmetros especificados
response = requests.get(url, headers=headers, params=parameters).text # Cria um objeto BeautifulSoup para fazer parsing do HTML retornado
soup = BeautifulSoup(response, 'html.parser')
return soup # Retorna o objeto BeautifulSoup

    # Chama a função para obter o conteúdo da página e armazena na variável 'page'

page = get_page_content(URL, HEADERS, PARAMETERS)

soup = get_page_content(URL, HEADERS, PARAMETERS)
table = soup.find('table')
print(table)

ta retornando none
