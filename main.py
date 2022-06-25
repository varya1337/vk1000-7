import vk_api
import os,time
from time import sleep
import datetime


def start():
    try:
        vk_auth = vk_api.VkApi(token="your token")
        vk = vk_auth.get_api()
        print("Авторизация прошла успешно")
    except:
        print("Ошибка авторизации")


    num = 1000
    while True:
        try:
            if num <= 0:
                num = 1000
            
            vk.status.set(text=f"{num} - 7")
            num-=7
            print("ворк")
        except:
            print("сука")
        break
    
    time.sleep(35)

    start()
    
start()