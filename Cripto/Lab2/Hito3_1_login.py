import _random
import email
from time import sleep
from tkinter import E, N, Button
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
Pass1="test1234"
Pass2="iman1234"
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



########## codigo para mas de un login ############

# driver = webdriver.Chrome('./chromedriver.exe', options=opts) # abre chrome y agrega taps con basura par tratar de distraer a los capchas 
# 
# driver = webdriver.Chrome('./chromedriver.exe') # abre solo chrome
# x=0
# for x in range(N):
#     driver.fullscreen_window
#     driver.get('https://www.lapolar.cl/Iniciar-Sesion/')
#     WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/div/main/div/div/div/div[6]/form/div[1]/input')))
#     imput_email= driver.find_element(By.XPATH,'/html/body/div[1]/div/main/div/div/div/div[6]/form/div[1]/input')
#     print("s1")
#     sleep(2)
#     imput_pass = driver.find_element(By.XPATH ,'/html/body/div[1]/div/main/div/div/div/div[6]/form/div[2]/input')
#     print("s2")
#     sleep(2)
#     imput_buton = driver.find_element(By.XPATH,'/html/body/div[1]/div/main/div/div/div/div[6]/form/div[4]/input')
#     print(Email[x],"\n")
#     print(Pass[x],"\n")
#     print("s3")
#     sleep(2)
#     imput_email.send_keys(Email[x])
#     print("s4")
#     sleep(2)
#     imput_pass.send_keys(Pass[x])
#     print("s5")
#     sleep(2)
#     imput_buton.click()
#     print("s6")
#     sleep(2)
#     WebDriverWait(driver,5)

####################################################
############## codigo para solo un user ############
####################################################

############## datos de ingreso ####################
Email="lucas.penailillo@mail.udp.cl"
Pass1="test1234"
Pass2="iman1234"
Nombre=""
Apellido=""
Telefono=""
Rut=""
####################################################
driver = webdriver.Chrome('./chromedriver.exe')
############# Register #############################
# print("Registrar usuario ..........")
# driver.get('https://www.lapolar.cl/Iniciar-Sesion/')
# WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/ul/li[2]/a')))
# imput_buton = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/ul/li[2]/a')
# print("sleep ",s)
# s+=1
# sleep(1)
# print("Haciendo click en el registro ........")
# imput_buton.click()
# WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/ul/li[2]/a')))
# imput_buton = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/form/button')
# print("sleep ",s)
# s+=1
# sleep(1)
# imput_nombre = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/form/div[2]/input')
# print("sleep ",s)
# s+=1
# sleep(1)
# imput_apellido = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/form/div[3]/input')
# print("sleep ",s)
# s+=1
# sleep(1)
# imput_Rut = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/form/div[5]/div/input')
# print("sleep ",s)
# s+=1
# sleep(1)
# imput_telefono = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/form/div[4]/div/div[2]/input')
# print("sleep ",s)
# s+=1
# sleep(1)
# imput_email = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/form/div[6]/input')
# print("sleep ",s)
# s+=1
# sleep(1)
# imput_checbox = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/form/div[7]/div[1]/div[1]/label/span')
# print("sleep ",s)
# s+=1
# sleep(1)
# imput_pass = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/form/div[8]/input')
# print("sleep ",s)
# s+=1
# sleep(1)
# imput_confirmpass = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/form/div[9]/input')
# print("sleep ",s)
# s+=1
# sleep(1)
# imput_checbox2 = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/form/div[10]/label')
# print("sleep ",s)
# s+=1
# sleep(1)
# print("insertar nombre ........")
# imput_nombre.send_keys(Nombre)
# print("sleep ",s)
# s+=1
# sleep(1)
# print("insertar Apellido ........")
# imput_apellido.send_keys(Apellido)
# print("sleep ",s)
# s+=1
# sleep(1)
# print("insertar Telefono ........")
# imput_telefono.send_keys(Telefono)
# print("sleep ",s)
# s+=1
# sleep(1)
# print("insertar RUT ........")
# imput_Rut.send_keys(Rut)
# print("sleep ",s)
# s+=1
# sleep(1)
# print("insertar correo electronico ........")
# imput_email.send_keys(Email)
# print("sleep ",s)
# s+=1
# sleep(1)
# print("seleccioner genero masculino ........")
# imput_checbox.click()
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
# print("deseleccionar los correos de spam ........")
# imput_checbox2.click()
# print("sleep ",s)
# s+=1
# sleep(1)
# print("click en finalizar registro ........")
# # imput_buton.click()




############## Olvidar Password ###################
print("olvidar contraseña .........")
driver.get('https://www.lapolar.cl/Iniciar-Sesion/')
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/form/div[6]/a')))
imput_buton= driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/form/div[6]/a')
print("sleep ",s)
s+=1
sleep(2)
print("Haciendo click olvidar password ........")
imput_buton.click()
sleep(5)
imput_email= driver.find_element(By.XPATH,'/html/body/div[8]/div[2]/div/div/form/div[1]/div[1]/div[2]/input')
s+=1
sleep(2)
imput_buton= driver.find_element(By.XPATH,'//*[@id="reset-password-email"]')
print("sleep ",s)
s+=1
sleep(2)
print("insertando Correo electronico  ........")
imput_email.send_keys(Email)
print("sleep ",s)
s+=1
sleep(2)
print("Haciendo click en enviar correo de recuperacion ........")
# imput_buton.click()

# # con correo termporal



# # gmail correo udp test
# driver.get("https://accounts.google.com/signin/v2/identifier?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&hl=es&flowName=GlifWebSignIn&flowEntry=ServiceLogin#__utma=29003808.887474793.1650405603.1650405603.1650405603.1&__utmb=29003808.0.10.1650405603&__utmc=29003808&__utmx=-&__utmz=29003808.1650405603.1.1.utmcsr=google%7Cutmccn=(organic)%7Cutmcmd=organic%7Cutmctr=(not%20provided)&__utmv=-&__utmk=92103769")
# WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')))
# imput_email = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
# print("sleep ",s)
# s+=1
# sleep(2)
# imput_email.send_keys(Email)

# sleep(5)







###################### Login #################
driver.get('https://www.lapolar.cl/Iniciar-Sesion/')
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/form/div[2]/input')))
imput_email= driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/form/div[2]/input')
print("sleep ",s)
s+=1
sleep(2)
imput_pass = driver.find_element(By.XPATH ,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/form/div[3]/input')
print("sleep ",s)
s+=1
sleep(2)
imput_buton = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/form/div[5]/button')
print("sleep ",s)
s+=1
sleep(2)
imput_recordar = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/form/div[4]/label')
print("sleep ",s)
s+=1
sleep(2)
print("ingresando email ....")
print(Email)
imput_email.send_keys(Email)
print("sleep ",s)
s+=1
sleep(2)
print("ingresando Password ....")
print(Pass1)
imput_pass.send_keys(Pass1)
print("sleep ",s)
s+=1
sleep(2)
print("Haciendo clic en recordar datos ....")
imput_recordar.click()
print("sleep ",s)
s+=1
sleep(2)
print("recargando pagina para ver si recuerda los datos ....")
driver.refresh()
print("sleep ",s)
s+=1
sleep(2)
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/form/div[2]/input')))
imput_email= driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/form/div[2]/input')
print("sleep ",s)
s+=1
sleep(2)
imput_pass = driver.find_element(By.XPATH ,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/form/div[3]/input')
print("sleep ",s)
s+=1
sleep(2)
imput_buton = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/form/div[5]/button')
print("sleep ",s)
s+=1
sleep(2)
imput_recordar = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/form/div[4]/label')
print("sleep ",s)
s+=1
sleep(2)
print("ingresando email ....")
print(Email)
imput_email.send_keys(Email)
print("sleep ",s)
s+=1
sleep(2)
print("ingresando Password ....")
print(Pass1)
imput_pass.send_keys(Pass1)
print("sleep ",s)
s+=1
sleep(2)
print("Haciendo clic en recordar datos ....")
imput_recordar.click()
print("sleep ",s)
s+=1
sleep(2)
print("Haciendo clic en Ingresar ....")
imput_buton.click()
WebDriverWait(driver,5)

print("Ahora a cambiar la contraseña por dentro ....")

############## Cambio Interno de contraseña ################
driver.get('https://www.lapolar.cl/Cambiar-clave/')
print("sleep ",s)
s+=1
sleep(5)
print("sleep ",s)
s+=1
sleep(4)
imput_pass = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[2]/div/div/form/div[1]/input')
print("sleep ",s)
s+=1
sleep(2)
imput_buton = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[2]/div/div/form/button')
print("sleep ",s)
s+=1
sleep(2)
imput_newpass = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[2]/div/div/form/div[2]/input')
print("sleep ",s)
s+=1
sleep(2)
imput_confirmpass = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[2]/div/div/form/div[3]/input')
print("sleep ",s)
s+=1
sleep(2)
print("ingresando Password actual ....")
print(Pass1)
imput_pass.send_keys(Pass1)
print("sleep ",s)
s+=1
sleep(2)
print("ingresando Password Nueva ....")
print(Pass2)
imput_newpass.send_keys(Pass2)
print("sleep ",s)
s+=1
sleep(2)
print("Confirmando Password Nueva ....")
print(Pass2)
imput_confirmpass.send_keys(Pass2)
print("sleep ",s)
s+=1
sleep(2)
print("Haciendo click en Actualizar contraseña ....")
# imput_buton.click()


sleep(4)
driver.close()


    # ## parte capcha lamentabla mente es manual
    # imput_pass= driver.find_element(By.XPATH,'/html/body/div[1]/div/main/div/div/div/div[6]/form/div[2]/input')
    # print("s7")
    #sleep(2)
    # Y = input("y para cuando el cacha esta check")
    # if Y is"y":
    #     print("s8")
        #sleep(2)
    #     imput_buton = driver.find_element(By.XPATH,'/html/body/div[1]/div/main/div/div/div/div[6]/form/div[4]/input')
    #     print("s9")
        #sleep(2)
    #     imput_pass.send_keys(Pass[x])
    #     print("s10")
        #sleep(2)
    #     imput_buton.click()
    #     print("s11")
        #sleep(2)