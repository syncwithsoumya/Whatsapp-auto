from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from customer_functions import *
from utilities import *
from admin_functions import *
import time
import sys


def send_admin_msg():
    try:
        msg = get_last_recent_msg(driver=driver)
        time.sleep(5)
        response = response_code_valid(str(msg))
        id = put_text(driver)
        id.clear()
        id.send_keys(response)
        id.send_keys(Keys.RETURN)
        time.sleep(1)
        click = click_default(driver=driver)
        click.click()

    except Exception as e:
        sender()


def send_msg():
    try:
        msg = get_last_recent_msg(driver=driver)
        time.sleep(5)
        user_type = get_user_type(driver)
        print user_type
        if user_type.startswith("superadmin"):
            response = admin_response_code_valid((str(msg)))
        else:
            response = response_code_valid(str(msg))
        id = put_text(driver)
        id.clear()
        id.send_keys(response)
        id.send_keys(Keys.RETURN)
        time.sleep(1)
        click = click_default(driver=driver)
        click.click()

    except Exception as e:
        sender()


def sender():
    time.sleep(20)
    try:
        e = click_notifications(driver=driver)
        ac = ActionChains(driver)
        ac.click(e).perform()
        send_msg()
    except:
        send_msg()


if __name__ == '__main__':
    sys.setrecursionlimit(5000)
    driver = webdriver.Chrome("chromedriver.exe")
    driver.maximize_window()
    driver.get("https://web.whatsapp.com/")
    while True:
        sender()
