import random
import notifiers
import selenium as selenium
import selenium.webdriver.common.by
from selenium import webdriver
import time
import os
import fake_useragent
from aiogram import types


ua = fake_useragent.UserAgent().random
option = webdriver.ChromeOptions()
option.add_argument(f"user-agent={ua}")
option.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
option.add_argument("--headless")
option.add_argument("--disable-dev-shm-usage")
option.add_argument("--no-sandbox")
option.headless = True

url = "https://uz-appointment.visametric.com/uz/appointment-form"
driver = webdriver.Chrome(executable_path="/home/otanazar/myprojects/selenium_project/chromedriver",
                          options=option)


# FUNCTION TO THE MESSAGE TO USERS
def send_to_users(text):
    tg = notifiers.get_notifier('telegram')
    my_id = [5568424899]
    id = [5070654961, 1997580715, 5609732776]
    for i in my_id:
        tg.notify(token="5476761946:AAGzXBfi-DOk3ZM3VttVmA6u8fbJ73nE_-4",
                  chat_id=i,
                  message=text)
    print('All Users Notified')


def parse(msg_from_bot=False):
    # START PARSING
    driver.get(url=url)
    # choosing resume
    NAMES = {"country": "",
             "visitingcountry": "",
             "city": "",
             "office": "",
             "officetype": "",
             "totalPerson": ""
             }

    for name, value in NAMES.items():
        index = 1
        if name == "city":
            index = random.randint(1, 18)
        resume = driver.find_element(selenium.webdriver.common.by.By.NAME, name).find_elements(
            selenium.webdriver.common.by.By.TAG_NAME, "option")[index]
        print(resume.text)
        resume.click()
        NAMES[name] = resume.text
        time.sleep(random.randint(2, 5))

    dates = driver.find_element(selenium.webdriver.common.by.By.ID, "availableDayInfo").find_element(
        selenium.webdriver.common.by.By.ID, "drs").find_elements(
        selenium.webdriver.common.by.By.TAG_NAME, "label"
    )

    # CHECKING DATES

    f = open("dates.txt", "r")
    t = f.read().split("\n")[:-1]
    changed = False
    can_send = True
    if len(f.read().split()) == 0:
        can_send = False
        changed = True
    else:
        can_send = True
        for n, i in enumerate(t):
            if i.strip() != dates[n].text:
                changed = True
                break
    f.close()
    # SENDING NEWS TO THE USERS
    if changed:
        result = ""
        f = open("dates.txt", "w")
        for i in dates:
            f.write(i.text + "\n")
            result += f"Ｓａｎａ:   {i.text}\n➖➖➖➖➖➖➖\n"
        f.close()
        if can_send:
            send_to_users("❗️❗️❗️🅂🄰🄽🄰 🄾'🅉🄶🄰🅁🄳🄸❗️❗️❗️\n\n" + result + f"\n𝚅𝚒𝚕𝚘𝚢𝚊𝚝:  {NAMES['city']}\n\n{url}")
        else:
            return "Yangi malumot topilmodi"
    else:
        if msg_from_bot:
            return "Yangi malumot topilmodi"



