from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import os
import xlsxwriter
import time as t
navegador = Chrome()
navegador.get('https://www.google.com.br')
t.sleep(4)
navegador.find_element('xpath','//*[@id="APjFqb"]').send_keys('dolar hj')
navegador.find_element('xpath','//*[@id="APjFqb"]').send_keys(Keys.RETURN)
dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text

navegador.get('https://www.google.com.br')
t.sleep(2)
navegador.find_element('xpath','//*[@id="APjFqb"]').send_keys('euro hj')
navegador.find_element('xpath','//*[@id="APjFqb"]').send_keys(Keys.RETURN)
euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
caminho = fr'C:\dolar e euro\DolareEuroGoogle.xlsx'
planilha = xlsxwriter.Workbook(caminho)
planilha1 = planilha.add_worksheet()
planilha1.write('A1', 'Dólar')
planilha1.write('B1', 'Euro')
planilha1.write('A2', dolar)
planilha1.write('B2', euro)
planilha.close()
os.startfile(caminho)
t.sleep(4)
