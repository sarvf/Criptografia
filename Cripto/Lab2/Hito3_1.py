import _random
import email
from re import A
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

Email=["lucas.penailillo@mail.udp.cl"]
Pass1=["test1234"]
Pass2=["iman1234"]
Nombre=[""]
Apellido=[""]
Telefono=[""]
Rut=[""]
s=1

data=[""]
data.clear()
Pass1.clear()
Pass2.clear()
Nombre.clear()
Apellido.clear()
Email.clear()
Rut.clear()
Telefono.clear()

file1 = open('./Hito3_1.txt',"r")
N=0
for i in file1:
    line = file1.readline()
    if line != "" :
        print(line,"\n")
        data = line.split(",")
        print(data,"\n")
        Pass1.append(data[1])
        Pass2.append(data[4])
        Nombre.append(data[5])
        Apellido.append(data[6])
        Email.append(data[2])
        Rut.append(data[3])
        Telefono.append(data[7])
        N+=1
file1.close

print(Email) #imprimir correo electronico o conjunto de correos cuando son mas de 1
print(Pass1) #imprimir contraseña o conjunto de contraseñas cuando son mas de 1
print(Pass2) #imprimir contraseña o conjunto de contraseñas cuando son mas de 1



############## datos de ingreso ####################
# Email="lucas.penailillo@mail.udp.cl"
# Pass1="test1234"
# Pass2="iman1234"
# Nombre=""
# Apellido=""
# Telefono=""
# Rut=""
####################################################
driver = webdriver.Chrome('./chromedriver.exe')
############# Register #############################
k=0
for k in range(N):
    print("Registrar usuario ..........")
    driver.get('https://www.lapolar.cl/Iniciar-Sesion/')
    WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/ul/li[2]/a')))
    imput_buton = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/ul/li[2]/a')
    print("sleep ",s)
    s+=1
    sleep(1)
    print("Haciendo click en el registro ........")
    imput_buton.click()
    WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/ul/li[2]/a')))
    imput_buton = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/form/button')
    print("sleep ",s)
    s+=1
    sleep(1)
    imput_nombre = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/form/div[2]/input')
    print("sleep ",s)
    s+=1
    sleep(1)
    imput_apellido = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/form/div[3]/input')
    print("sleep ",s)
    s+=1
    sleep(1)
    imput_Rut = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/form/div[5]/div/input')
    print("sleep ",s)
    s+=1
    sleep(1)
    imput_telefono = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/form/div[4]/div/div[2]/input')
    print("sleep ",s)
    s+=1
    sleep(1)
    imput_email = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/form/div[6]/input')
    print("sleep ",s)
    s+=1
    sleep(1)
    imput_checbox = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/form/div[7]/div[1]/div[1]/label/span')
    print("sleep ",s)
    s+=1
    sleep(1)
    imput_pass = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/form/div[8]/input')
    print("sleep ",s)
    s+=1
    sleep(1)
    imput_confirmpass = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/form/div[9]/input')
    print("sleep ",s)
    s+=1
    sleep(1)
    imput_checbox2 = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/form/div[10]/label')
    print("sleep ",s)
    s+=1
    sleep(1)
    print("insertar nombre ........")
    imput_nombre.send_keys(Nombre[k])
    print("sleep ",s)
    s+=1
    sleep(1)
    print("insertar Apellido ........")
    imput_apellido.send_keys(Apellido[k])
    print("sleep ",s)
    s+=1
    sleep(1)
    print("insertar Telefono ........")
    imput_telefono.send_keys(Telefono[k])
    print("sleep ",s)
    s+=1
    sleep(1)
    print("insertar RUT ........")
    imput_Rut.send_keys(Rut[k])
    print("sleep ",s)
    s+=1
    sleep(1)
    print("insertar correo electronico ........")
    imput_email.send_keys(Email[k])
    print("sleep ",s)
    s+=1
    sleep(1)
    print("seleccioner genero masculino ........")
    imput_checbox.click()
    print("sleep ",s)
    s+=1
    sleep(1)
    print("insertar password ........")
    imput_pass.send_keys(Pass1[k])
    print("sleep ",s)
    s+=1
    sleep(1)
    print("insertar password nuevamente ........")
    imput_confirmpass.send_keys(Pass1[k])
    print("sleep ",s)
    s+=1
    sleep(1)
    print("deseleccionar los correos de spam ........")
    imput_checbox2.click()
    print("sleep ",s)
    s+=1
    sleep(1)
    print("click en finalizar registro ........")
    imput_buton.click()




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
    imput_email.send_keys(Email[k])
    print("sleep ",s)
    s+=1
    sleep(2)
    print("Haciendo click en enviar correo de recuperacion ........")
    imput_buton.click()

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
    imput_email.send_keys(Email[k])
    print("sleep ",s)
    s+=1
    sleep(2)
    print("ingresando Password ....")
    print(Pass1)
    imput_pass.send_keys(Pass1[k])
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
    imput_email.send_keys(Email[k])
    print("sleep ",s)
    s+=1
    sleep(2)
    print("ingresando Password ....")
    print(Pass1)
    imput_pass.send_keys(Pass1[k])
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



    ############## Cambio Interno de contraseña ################
    print("sleep ",s)
    s+=1
    sleep(2)
    print("Ahora a cambiar la contraseña por dentro ....")
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
    print(Pass1[k])
    imput_pass.send_keys(Pass1[k])
    print("sleep ",s)
    s+=1
    sleep(2)
    print("ingresando Password Nueva ....")
    print(Pass2[k])
    imput_newpass.send_keys(Pass2[k])
    print("sleep ",s)
    s+=1
    sleep(2)
    print("Confirmando Password Nueva ....")
    print(Pass2[k])
    imput_confirmpass.send_keys(Pass2[k])
    print("sleep ",s)
    s+=1
    sleep(2)
    print("Haciendo click en Actualizar contraseña ....")
    imput_buton.click()
    sleep(4)
driver.close()
