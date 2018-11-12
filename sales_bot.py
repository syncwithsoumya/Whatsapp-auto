from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
import time
import sys


def check_user_needs():
    menu = """
    Hello ! I can help you with the below options
    1. Lodge a complaint
    2. Check complaint status
    3. Request a callback
    Please only type out the required option and I will assist you. 
    [Note: We may be slow in responding please wait a while before placing 2nd request]
    """
    return menu


def response_code_valid(service=None):
    data = str(service.lower()).split(" ")
    print data
    if len(data) > 1:
        for i in range(0,len(data)):
            print data[i] in ['issue', 'issues', 'problem', 'problems', 'help', 'fix']
            if data[i] in ['issue', 'issues', 'problem', 'problems', 'help', 'fix']:
                response = check_user_needs()
                break
            elif i == len(data)-1:
                response = selected_service(service)
    elif service in ['1', '2', '3'] or service.lower().startswith("ref"):
        response = selected_service(service)
    else:
        response = 'Could n\'t understand you. Please request with texts e.g help me, i need fix or etc..'
    return response


def selected_service(service=None):
    bool = service.lower().startswith("ref")
    print bool
    if service == '1':
        num = randint(999,9999)
        response = complaint(num)
    elif service == '2' or bool:
        response = status(service)
    elif service == '3':
        response = callback()
    else:
        response = 'Incorrect Response Code. Please try again'

    return response


def complaint(number=None):
    sample_code = 'REF{}'.format(number)
    msg = "You complaint is filed under Reference Number - {}".format(sample_code)
    return msg


def status(code=None):
    if code == '2':
        return "Please share your ref number"
    else:
        return "Your reference number is under process."


def callback():
    return "Your number is registered and you will receive a callback as soon as possible"


def send_msg():
    try:

        cc = driver.find_elements_by_xpath("//span[@class='selectable-text invisible-space copyable-text']")
        print "len",len(cc)
        # dc = driver.find_elements_by_xpath("//*[@class='_3_7SH _3DFk6 message-out']//*[@class='selectable-text invisible-space copyable-text']")
        # print "DC -> {}" .format(dc.text)
        # e = driver.find_element_by_xpath("//div[.//span[@class='selectable-text invisible-space copyable-text']]/ancestor::div[@class='_3zb-j ZhF0n']/ancestor::div[@class='copyable-text']/ancestor::div[@class='Tkt2p']/ancestor::div[@class='_3_7SH _3DFk6 message-in tail']")
        # print e
        for i in range(0,len(cc)):
            msg = driver.find_element_by_xpath("(//span[@class='selectable-text invisible-space copyable-text'])[position()={}]".format(i+1))
            print (msg.text)
            # print dc

        time.sleep(5)
        # response = response_code_valid(str(msg.text))
        # id = driver.find_element_by_css_selector("._2S1VP.copyable-text.selectable-text")
        # id.clear()
        # id.send_keys(response)
        # id.send_keys(Keys.RETURN)
        # time.sleep(1)
        # clic = driver.find_element_by_xpath("//span[contains(text(), 'Prachi')]")
        # # print (clic)
        # clic.click()

    except Exception as e:
        sender()


def sender():
    time.sleep(20)
    try:
        e = driver.find_element_by_xpath("//div[.//span[@class='OUeyt']]/ancestor::div[@class='_3j7s9']")
        ac = ActionChains(driver)
        ac.click(e).perform()
        send_msg()
    except:
        # print ("Exception")
        send_msg()


if __name__ == '__main__':
    sys.setrecursionlimit(5000)
    driver = webdriver.Chrome("chromedriver.exe")
    driver.maximize_window()
    driver.get("https://web.whatsapp.com/")
    while True:
        sender()
