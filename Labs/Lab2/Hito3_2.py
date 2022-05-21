from time import sleep
from pandas import RangeIndex
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
opts= Options()
opts.add_argument("Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36")

# correos temporales
# https://temp-mail.org/es/
#
#

# https://correotemporal.org/
# kamren52x_h805x@hxsni.com
# test12

# rut aleatorios
# http://jqueryrut.sourceforge.net/generador-de-ruts-chilenos-validos.html

Email="lucas.penailillo@mail.udp.cl"
Pass1="iman1234"
Pass2="test1234"
s=1
# Pass= [""]
# Email=[""]
# data=[""]
# data.clear()
# Pass.clear()
# Email.clear()
# file1 = open('./Hito1.txt',"r")
# file1.readline()
# file1.readline()
# N=0
# for i in file1:
#     line = file1.readline()
#     if line != "" :
#         print(line,"\n")
#         data = line.split(",")
#         print(data,"\n")
#         Pass.append(data[1]) 
#         Email.append(data[2])
#         N+=1
# file1.close
print(Email) #imprimir correo electronico o conjunto de correos cuando son mas de 1
print(Pass1) #imprimir contraseña o conjunto de contraseñas cuando son mas de 1
print(Pass2) #imprimir contraseña o conjunto de contraseñas cuando son mas de 1


####################################################
############## codigo para solo un user ############
####################################################

############## datos de ingreso ####################
# Email="lucas.penailillo@mail.udp.cl"
# Pass2="iman1234"
# Pass1="test1234"
User="sarvf"
Activacion=""
Pass1="hola1234"
Pass2="test1234"

Email="lucaspenailillomoreno@gmail.com"
# Pass2="hola1234"
# Pass1="test1234"
# User="sarvft"
# Activacion=""
####################################################
driver = webdriver.Chrome('./chromedriver.exe')
############# Register #############################
# print("Registrar usuario ..........")
# driver.get('http://wow.wowaura.com/index.php')
# WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[4]/td/input[2]')))
# imput_buton = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[4]/td/input[2]')
# print("sleep ",s)
# s+=1
# sleep(1)
# print("Haciendo click en el registro ........")
# imput_buton.click()
# WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input')))
# imput_buton = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[3]/td/input[1]')
# print("sleep ",s)
# s+=1
# sleep(1)
# imput_email = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input')
# print("sleep ",s)
# s+=1
# sleep(1)
# print("insertar correo electronico ........")
# imput_email.send_keys(Email)
# print("sleep ",s)
# s+=1
# sleep(1)
# print("Haciendo click en continuar ........")
# imput_buton.click()
# print("sleep ",s)
# s+=1
# sleep(1)
# print("Esperando terminos y condiciones ........")
# j=0
# for j in range(61):
#     sleep(2)
#     print("quedan ",122-2*j," segundos")
# print("Haciendo click en continuar ........")
# imput_buton = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[3]/td/div[1]')
# print("sleep ",s)
# s+=1
# sleep(5)
# imput_user = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]/input')
# print("sleep ",s)
# s+=1
# sleep(1)
# imput_pass = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td[2]/input')
# print("sleep ",s)
# s+=1
# sleep(1)
# imput_confirmpass = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td[2]/input')
# print("sleep ",s)
# s+=1
# sleep(1)
# imput_email = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/table/tbody/tr[4]/td[2]/input')
# print("sleep ",s)
# s+=1
# sleep(1)
# imput_activacion = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]/input')
# print("sleep ",s)
# s+=1
# sleep(1)
# imput_buton = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[3]/td/input')
# print("sleep ",s)
# s+=1
# sleep(1)
# print("insertar Username ........")
# imput_user.send_keys(User)
# print("sleep ",s)
# s+=1
# sleep(1)
# print("insertar password ........")
# imput_pass.send_keys(Pass1)
# print("sleep ",s)
# s+=1
# sleep(1)
# print("insertar password nuevamente ........")
# imput_confirmpass.send_keys(Pass1)
# print("sleep ",s)
# s+=1
# sleep(1)
# print("insertar correo electronico ........")
# imput_email.send_keys(Email)
# print("sleep ",s)
# s+=1
# sleep(1)
# print("insertar Activacion ........")
# imput_activacion.send_keys(Activacion)
# print("sleep ",s)
# s+=1
# sleep(1)
# print("click en finalizar registro ........")
# # imput_buton.click()




# ############## Olvidar Password ###################
print("olvidar contraseña .........")
driver.get('http://wow.wowaura.com/index.php')
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td/a')))
imput_buton= driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td/a')
print("sleep ",s)
s+=1
sleep(2)
print("Haciendo click olvidar password ........")
imput_buton.click()
sleep(5)
imput_us= driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input')
s+=1
sleep(2)
imput_email= driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input')
s+=1
sleep(2)
imput_buton= driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td/input[1]')
print("sleep ",s)
s+=1
sleep(2)
print("insertando Username  ........")
imput_us.send_keys(User)
# print("sleep ",s)
# s+=1
# sleep(2)
# print("insertando Correo electronico  ........")
# imput_email.send_keys(Email)
print("sleep ",s)
s+=1
sleep(2)
print("Haciendo click en enviar correo de recuperacion ........")
imput_buton.click()
# ################## correos de confirmacion #############


# # # con correo termporal



# # # gmail correo udp test
# # driver.get("https://accounts.google.com/signin/v2/identifier?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&hl=es&flowName=GlifWebSignIn&flowEntry=ServiceLogin#__utma=29003808.887474793.1650405603.1650405603.1650405603.1&__utmb=29003808.0.10.1650405603&__utmc=29003808&__utmx=-&__utmz=29003808.1650405603.1.1.utmcsr=google%7Cutmccn=(organic)%7Cutmcmd=organic%7Cutmctr=(not%20provided)&__utmv=-&__utmk=92103769")
# # WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')))
# # imput_email = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
# # print("sleep ",s)
# # s+=1
# # sleep(2)
# # imput_email.send_keys(Email)

# # sleep(5)

########################################################





# ###################### Login #################
driver.get('http://wow.wowaura.com/index.php')
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input')))
imput_user= driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input')
print("sleep ",s)
s+=1
sleep(2)
imput_pass = driver.find_element(By.XPATH ,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input')
print("sleep ",s)
s+=1
sleep(2)
imput_buton = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[4]/td/input[1]')
print("sleep ",s)
s+=1
sleep(2)
print("ingresando email ....")
print(User)
imput_user.send_keys(User)
print("sleep ",s)
s+=1
sleep(2)
print("ingresando Password ....")
print(Pass1)
imput_pass.send_keys(Pass1)
print("sleep ",s)
s+=1
sleep(2)
print("Haciendo clic en Ingresar ....")
imput_buton.click()
WebDriverWait(driver,5)



# ############## Cambio Interno de contraseña ################
print("sleep ",s)
s+=1
sleep(2)
print("Ahora a cambiar la contraseña por dentro ....")
imput_buton = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td[1]/span')
print("sleep ",s)
s+=1
sleep(2)
print("Haciendo click en el server  ....")
imput_buton.click()
print("sleep ",s)
s+=1
sleep(2)
imput_buton = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/img')
print("sleep ",s)
s+=1
sleep(2)
print("Haciendo click en Mi Cuenta ....")
imput_buton.click()
print("sleep ",s)
s+=1
sleep(2)
imput_buton = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td[1]/table/tbody/tr[2]/td/img')
print("sleep ",s)
s+=1
sleep(2)
print("Haciendo click en Cambiar Contraseña ....")
imput_buton.click()
print("sleep ",s)
s+=1
sleep(2)
imput_pass = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/input')
print("sleep ",s)
s+=1
sleep(2)
imput_confirmpass = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[4]/td[2]/input')
print("sleep ",s)
s+=1
sleep(2)
imput_buton = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[5]/td/input')
print("sleep ",s)
s+=1
sleep(2)
print("ingresando Nueva Contraseña ....")
imput_pass.send_keys(Pass2)
print("sleep ",s)
s+=1
sleep(2)
print("Confirmando Nueva Contraseña ....")
imput_confirmpass.send_keys(Pass2)
print("sleep ",s)
s+=1
sleep(2)
print("Haciendo click en solicitar Cambio....")
imput_buton.click()

################## correos de confirmacion #############

########################################################



driver.close()