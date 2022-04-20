import _random
from time import sleep
from tkinter import E, N, Button
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
opts= Options()
opts.add_argument("Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36")


Pass= [""]
Email=[""]
data=[""]
data.clear()
Pass.clear()
Email.clear()
file1 = open('./Hito1.txt',"r")
file1.readline()
file1.readline()
N=0
for i in file1:
    line = file1.readline()
    if line != "" :
        print(line,"\n")
        data = line.split(",")
        print(data,"\n")
        Pass.append(data[1]) 
        Email.append(data[2])
        N+=1
file1.close
print(Email,"\n") 
print(Pass,"\n")
# driver = webdriver.Chrome('./chromedriver.exe', options=opts)
driver = webdriver.Chrome('./chromedriver.exe')
x=0
for x in range(N):
    driver.fullscreen_window
    driver.get('https://www.educarchile.cl/user/login')
    WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/div/main/div/div/div/div[6]/form/div[1]/input')))
    imput_email= driver.find_element(By.XPATH,'/html/body/div[1]/div/main/div/div/div/div[6]/form/div[1]/input')
    print("s1")
    sleep(2)
    imput_pass = driver.find_element(By.XPATH ,'/html/body/div[1]/div/main/div/div/div/div[6]/form/div[2]/input')
    print("s2")
    sleep(2)
    imput_buton = driver.find_element(By.XPATH,'/html/body/div[1]/div/main/div/div/div/div[6]/form/div[4]/input')
    print(Email[x],"\n")
    print(Pass[x],"\n")
    print("s3")
    sleep(2)
    imput_email.send_keys(Email[x])
    print("s4")
    sleep(2)
    imput_pass.send_keys(Pass[x])
    print("s5")
    sleep(2)
    imput_buton.click()
    print("s6")
    sleep(2)
    WebDriverWait(driver,5)

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