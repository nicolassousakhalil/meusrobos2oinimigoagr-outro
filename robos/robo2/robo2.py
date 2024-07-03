from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time as t

navegador = Chrome()
navegador.get('https://buscacepinter.correios.com.br/app/endereco/index.php')
t.sleep(2)
navegador.find_element('xpath','//*[@id="endereco"]').send_keys('05892387')
navegador.find_element('xpath', '//*[@id="btn_pesquisar"]').click()
t.sleep(2)
rua = navegador.find_element('xpath', '//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text
bairro = navegador.find_element('xpath', '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
cidade = navegador.find_element('xpath', '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text
cep = navegador.find_element('xpath', '//*[@id="resultado-DNEC"]/tbody/tr/td[4]').text
print(rua)
print(bairro)
print(cidade)
print(cep)

print('teste')
print('outra coisa')