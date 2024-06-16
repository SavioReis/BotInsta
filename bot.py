from selenium import webdriver
import time
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() #abrir chrome
driver.get('https://www.instagram.com/')
time.sleep(5)

################
##### Cola
################
#driver.find_element(By.XPATH,VARIAVEL)
#driver.find_element(By.CLASS_NAME,VARIAVEL)
#driver.find_element(By.TAG_NAME,VARIAVEL)

################
#Variaveis
################
campo_login = '//*[@id="loginForm"]/div/div[1]/div/label/input'
campo_senha = '//*[@id="loginForm"]/div/div[2]/div/label/input'
notificacao_class = '_a9_1'
bolinha_notificacao = 'xzolkzo'
msg_class_padrao = 'x9f619'
contato_cliente =  'xuxw1ft'
msg = 'x126k92a'
responder = 'xisnujt'

################
#####LOGAR INSTAGRAM
################
login = driver.find_element(By.XPATH,campo_login)
login.click()
login.send_keys('email_login@gmail.com') #email para conectar a conta do bot
time.sleep(1)
senha = driver.find_element(By.XPATH,campo_senha)
senha.click()
senha.send_keys('senha') #senha da conta
time.sleep(1)
senha.send_keys(Keys.ENTER)

################
#####Entrando area de chat e clicando em não nas notificações
################
time.sleep(5)
driver.get('https://www.instagram.com/direct/inbox/')
notificacao = driver.find_element(By.CLASS_NAME,notificacao_class)
time.sleep(1)
notificacao.click()


################
#####Função do bot
################
def bot():
    try:
        ################
        #####Clicar na bolinha de mensagem
        ################
        bolinha = driver.find_element(By.CLASS_NAME,bolinha_notificacao)
        bolinha = driver.find_elements(By.CLASS_NAME,bolinha_notificacao)
        clica_bolinha = bolinha[-1]#clicar na ultima mensagem    
        acao_bolinha = webdriver.common.action_chains.ActionChains(driver) 
        acao_bolinha.move_to_element_with_offset(clica_bolinha,0,-20)
        acao_bolinha.click()
        acao_bolinha.perform()
        time.sleep(3)
        print('clicou na bolinha')
        #######################################################

        ################
        #####Pegar nome do contato
        ################   
        contato = driver.find_elements(By.CLASS_NAME,contato_cliente)
        contato_final = contato[8]
        contato2 = contato_final.text
        print(contato2)
        print('peguei o contato')

        ################
        #####Pegar mensagem
        ################           
        todas_as_mensagens = driver.find_elements(By.CLASS_NAME,msg)
        todas_as_mensagens_texto = [e.text for e in todas_as_mensagens]
        msg_final = todas_as_mensagens_texto[-1]
        print(msg_final)
        time.sleep(2)
        print('Peguei a mensagem')

        ############
        #####Responder mensagem
        ################
        textarea = driver.find_element(By.CLASS_NAME,responder)
        textarea.send_keys("Olá, sou um bot de atendimento desenvolvido pelo programador Sávio Reis. Em que posso ajudar você?", Keys.ENTER)
        time.sleep(3)
        print('Mensagem respondida')
        ############
        #####Voltar mensagem padrão depois de ler a mensagem
        ################
        msg_padrao = driver.find_elements(By.CLASS_NAME,msg_class_padrao)
        msgpadrao_final = msg_padrao[24]
        time.sleep(3)
        msgpadrao_final.click()

    except:
        print('aguarde')
        time.sleep(1)

while True: 
    bot()