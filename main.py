import vk_api
import os,time
from time import sleep


def start():
    try:
        vk_auth = vk_api.VkApi(token="your token")
        vk = vk_auth.get_api()
        print("good")
    except:
        print("give me a new token or wait a 5 min")


    num = 1000
    while True:
        try:
            if num <= 0:
                num = 1000
            
            vk.status.set(text=f"{num} - 7")
            num-=7
            print("work")
        except:
            print("nevermind his didnt work")
            break
    time.sleep(35)

    start()
    
start()
