from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time as t
from openpyxl import load_workbook
arquivo = fr'C:\Users\nicolas.khalil\Downloads\DadosFormulario.xlsx'
planilha_aberta = load_workbook(filename=arquivo)
planilha = planilha_aberta['Dados']
for linha in range (2, len(planilha['A'])+1):
    nome = planilha[f'A{linha}'].value
    email = planilha[f'B{linha}'].value
    telefone = planilha[f'C{linha}'].value
    sexo = planilha[f'D{linha}'].value
    algo = planilha[f'E{linha}'].value

    navegador = Chrome()
    navegador.get('https://pt.surveymonkey.com/r/WLXYDX2')

    espera = WebDriverWait(navegador,10)

    campo_nome = espera.until(EC.presence_of_element_located((By.XPATH, '//*[@id="166517069"]')))
    campo_nome.send_keys(nome)

    campo_email = espera.until(EC.presence_of_element_located((By.XPATH, '//*[@id="166517072"]')))
    campo_email.send_keys(email)
    campo_telefone = espera.until(EC.presence_of_element_located((By.XPATH, '//*[@id="166517070"]')))
    campo_telefone.send_keys(telefone)
    campo_algo = espera.until(EC.presence_of_element_located((By.XPATH, '//*[@id="166517073"]')))
    campo_algo.send_keys(algo)
    #esse presence pra rodar direito precisa estar em tuplas/parenteses duplos '((jijj))'
    if sexo == 'Masculino':
        masculino = espera.until(EC.presence_of_element_located((By.XPATH, '//*[@id="166517071_1215509812_label"]')))
        masculino.click()
    else:
        feminino = espera.until(EC.presence_of_element_located((By.XPATH, '//*[@id="166517071_1215509813_label"]')))
        feminino.click()
    enviar = espera.until(EC.presence_of_element_located((By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button')))
    enviar.click()
    t.sleep(3)


print('teste')
print('algm coisa')