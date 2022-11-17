import os
import webbrowser
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import threading

# import subprocess

import voice

# try:
#     import requests  # pip install requests
# except:
#     pass


def browser():
    '''Открывает браузер заданнный по уполчанию в системе с url указанным здесь'''

    webbrowser.open('https://www.youtube.com', new=2)


# def game():
#     '''Нужно разместить путь к exe файлу любого вашего приложения'''
#     try:
#         subprocess.Popen('C:/Program Files/paint.net/PaintDotNet.exe')
#     except:
#         voice.speaker('Путь к файлу не найден, проверьте, правильный ли он')


def offpc():
    # Эта команда отключает ПК под управлением Windows

    os.system('shutdown \s')
    print('пк был бы выключен, но команде # в коде мешает;)))')


# def weather():
#     '''Для работы этого кода нужно зарегистрироваться на сайте
#     https://openweathermap.org или переделать на ваше усмотрение под что-то другое'''
#     try:
#         params = {'q': 'London', 'units': 'metric', 'lang': 'ru', 'appid': 'ключ к API'}
#         response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
#         if not response:
#             raise
#         w = response.json()
#         voice.speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")
#
#     except:
#         voice.speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')


def offBot():
    '''Отключает бота'''
    sys.exit()





# Вход в Игру





#Деревня в центре





def Farm():
    # print(a+b)


    my_login = ""
    my_password = ""
    url = ""

    assert my_login != '', ValueError()
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get(url=url)

    flag = False
    while flag == False:
        try:
            driver.implicitly_wait(10)
            apply = driver.find_element(By.CSS_SELECTOR, "a[class*= cmptxt_btn_yes]").click()
            loginButton = driver.find_element(By.CSS_SELECTOR, "div[class*= loginButtonContainer]").click()
            driver.implicitly_wait(7)

            frameElement = driver.find_element(By.CSS_SELECTOR, "#mellonModal iframe")
            driver.switch_to.frame(frameElement)

            sleep(10)

            iframe2 = driver.find_element(By.TAG_NAME, "iframe")
            driver.switch_to.frame(iframe2)

            sleep(5)

            emailInput = driver.find_element(By.NAME, "email")
            emailInput.send_keys(my_login)

            pwdInput = driver.find_element(By.NAME, "password")
            pwdInput.send_keys(my_password)

            driver.find_element(By.NAME, "submit").click()
            driver.implicitly_wait(10)
            sleep(10)
            btn = driver.find_element(By.CSS_SELECTOR, "div[class*= last-active-game-world] button ").click()
            flag = True
            return driver

        except:
            flag = False
            print("Невозможно подключиться")
            sleep(10)

    while True:
        # # Grenny = 100
        try:
        #     if Grenny >= 70:
        #         pass
        #         driver.implicitly_wait(10)
        #         troops = driver.find_element(By.CSS_SELECTOR, "i[class*=building_g19_small_flat_green]").click()
        #         driver.implicitly_wait(10)
        #         sleep(3)
        #         maxButton = driver.find_element(By.CSS_SELECTOR, "div[class*= maxButton]").click()
        #         driver.implicitly_wait(10)
        #         sleep(3)
        #         maxButton = driver.find_element(By.CSS_SELECTOR, "div[class*= maxButton]").click()
        #         driver.implicitly_wait(10)
        #         sleep(3)
        #         bilding= driver.find_element(By.CSS_SELECTOR, "button[class*=footerButton]").click()
        #         driver.implicitly_wait(10)
        #
        #         sleep(10)
        #         NPC = driver.find_element(By.XPATH, "/html/body/div[3]/window/div/div/div[4]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/npc-trader-button/div").click()
        #         sleep(3)
        #         driver.implicitly_wait(10)
        #         bilding_NPC = driver.find_element(By.XPATH, """//*[@id="npcMerchantOverlay"]/div[2]/div/div[2]/div/div/div[3]/div[1]/button""").click()
        #         sleep(3)
        #         driver.implicitly_wait(10)
        #         maxButton = driver.find_element(By.CSS_SELECTOR, "div[class*= maxButton]").click()
        #         driver.implicitly_wait(10)
        #         bilding = driver.find_element(By.CSS_SELECTOR, "button[class*=footerButton]").click()
        #
        #     else:
            driver.implicitly_wait(5)
            farm = driver.find_element(By.CSS_SELECTOR, "a[class*= troop]").click()
            driver.implicitly_wait(10)
            farm1 = driver.find_element(By.CSS_SELECTOR, "a[class*= naviTabFarmList]").click()
            driver.implicitly_wait(10)
            input_check_box = WebDriverWait(driver, 15).until(
                        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "td[class*=selector]")))
            input_check_box[1].click()
            driver.implicitly_wait(10)
            buttn = driver.find_element(By.CSS_SELECTOR, "button[class*=startRaid]").click()
            driver.implicitly_wait(10)
            buttn_clous = driver.find_element(By.CSS_SELECTOR, "a[class*=closeWindow]")

            time_sleep = random.randint(180, 600)
            # print(f"{time_sleep} Войска отправлены на смерть")
            sleep(time_sleep)
        except:
            print("что то пошло не так")
            sleep(10)
            continue



def new_farm():
    return threading.Thread(target=Farm,daemon=True).start()



def passive():
    pass

def new_passive():
    threading.Thread(target=passive, daemon=True).start()

